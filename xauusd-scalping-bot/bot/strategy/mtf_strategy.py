"""Otak robot: strategi multi-timeframe H1 -> M15 -> M5.

Alur (meniru cara trading manual: cek trend H1, gambar chart M15, entry M5):
  1. H1  : trend via EMA50/EMA200 + struktur swing (HH/HL vs LH/LL)
  2. M15 : harga harus sedang pullback ke "value zone" searah trend
  3. M5  : trigger candle konfirmasi (engulfing / pin bar) + filter RSI
"""
from dataclasses import dataclass
from datetime import datetime, time as dtime

import pandas as pd

from . import indicators as ind


@dataclass
class Signal:
    side: str        # "BUY" / "SELL"
    entry: float     # harga acuan entry (close M5 terakhir; live pakai ask/bid)
    sl: float
    tp: float
    reason: str      # penjelasan sinyal (dikirim ke Telegram)
    time: datetime


class MTFStrategy:
    def __init__(self, cfg):
        self.cfg = cfg.strategy

    # ---------- Langkah 1: trend H1 ----------
    def h1_trend(self, h1: pd.DataFrame) -> str:
        c = self.cfg
        close = h1["close"]
        ema_fast = ind.ema(close, c["ema_fast"]).iat[-1]
        ema_slow = ind.ema(close, c["ema_slow"]).iat[-1]
        price = close.iat[-1]
        structure = ind.structure_bias(h1, c["swing_lookback"])

        if ema_fast > ema_slow and price > ema_fast and structure != "bearish":
            return "bullish"
        if ema_fast < ema_slow and price < ema_fast and structure != "bullish":
            return "bearish"
        return "neutral"

    # ---------- Langkah 2: pullback ke value zone di M15 ----------
    def m15_in_zone(self, m15: pd.DataFrame, trend: str) -> bool:
        """Harga dianggap "di zona" kalau candle M15 terakhir menyentuh area
        antara EMA20 dan EMA50 M15 (area diskon dalam trend), atau menyentuh
        zona swing terdekat (tebal zona = zone_atr_mult x ATR M15)."""
        c = self.cfg
        close = m15["close"]
        ema20 = ind.ema(close, 20).iat[-1]
        ema50 = ind.ema(close, 50).iat[-1]
        atr15 = ind.atr(m15, c["atr_period"]).iat[-1]
        zone_w = c["zone_atr_mult"] * atr15
        last = m15.iloc[-1]
        highs, lows = ind.swing_points(m15, c["swing_lookback"])

        if trend == "bullish":
            band_lo, band_hi = min(ema20, ema50), max(ema20, ema50)
            touched_band = last["low"] <= band_hi and last["high"] >= band_lo
            touched_swing = any(
                abs(last["low"] - p) <= zone_w for _, p in lows[-3:]
            )
            return touched_band or touched_swing
        if trend == "bearish":
            band_lo, band_hi = min(ema20, ema50), max(ema20, ema50)
            touched_band = last["high"] >= band_lo and last["low"] <= band_hi
            touched_swing = any(
                abs(last["high"] - p) <= zone_w for _, p in highs[-3:]
            )
            return touched_band or touched_swing
        return False

    # ---------- Langkah 3: trigger di M5 ----------
    def m5_trigger(self, m5: pd.DataFrame, trend: str):
        """Return (ok, nama_pola). Dievaluasi pada candle M5 TERAKHIR YANG SUDAH
        CLOSE (index -1 — caller wajib mengirim df tanpa candle yang masih jalan)."""
        c = self.cfg
        i = len(m5) - 1
        rsi_now = ind.rsi(m5["close"], c["rsi_period"]).iat[-1]

        if trend == "bullish":
            if rsi_now >= c["rsi_overbought"]:
                return False, "RSI overbought"
            if ind.is_bullish_engulfing(m5, i):
                return True, "bullish engulfing"
            if ind.is_bullish_pinbar(m5, i):
                return True, "bullish pin bar"
        elif trend == "bearish":
            if rsi_now <= c["rsi_oversold"]:
                return False, "RSI oversold"
            if ind.is_bearish_engulfing(m5, i):
                return True, "bearish engulfing"
            if ind.is_bearish_pinbar(m5, i):
                return True, "bearish pin bar"
        return False, ""

    # ---------- Filter sesi ----------
    def in_session(self, now_local: datetime) -> bool:
        c = self.cfg
        start = dtime.fromisoformat(c["session_start"])
        end = dtime.fromisoformat(c["session_end"])
        t = now_local.time()
        if not (start <= t <= end):
            return False
        if now_local.weekday() == 4:  # Jumat: hindari jelang weekend
            if t >= dtime.fromisoformat(c["no_trade_friday_after"]):
                return False
        return True

    # ---------- Gabungan ----------
    def evaluate(self, h1: pd.DataFrame, m15: pd.DataFrame, m5: pd.DataFrame,
                 now_local: datetime):
        """Return Signal atau None. Semua df = candle yang sudah close saja."""
        c = self.cfg
        if not self.in_session(now_local):
            return None

        trend = self.h1_trend(h1)
        if trend == "neutral":
            return None
        if not self.m15_in_zone(m15, trend):
            return None
        ok, pattern = self.m5_trigger(m5, trend)
        if not ok:
            return None

        atr5 = ind.atr(m5, c["atr_period"]).iat[-1]
        entry = float(m5["close"].iat[-1])
        _, lows = ind.swing_points(m5, c["swing_lookback"])
        highs, _ = ind.swing_points(m5, c["swing_lookback"])

        if trend == "bullish":
            base_sl = lows[-1][1] if lows else float(m5["low"].tail(10).min())
            sl = base_sl - c["sl_buffer_atr"] * atr5
            sl = min(sl, entry - c["sl_min_atr"] * atr5)  # SL minimal 1 ATR
            dist = entry - sl
            tp = entry + c["risk_reward"] * dist
            side = "BUY"
        else:
            base_sl = highs[-1][1] if highs else float(m5["high"].tail(10).max())
            sl = base_sl + c["sl_buffer_atr"] * atr5
            sl = max(sl, entry + c["sl_min_atr"] * atr5)
            dist = sl - entry
            tp = entry - c["risk_reward"] * dist
            side = "SELL"

        reason = (
            f"H1 trend {trend} (EMA{c['ema_fast']}/{c['ema_slow']} + struktur), "
            f"pullback zona M15, trigger M5: {pattern}"
        )
        return Signal(side=side, entry=entry, sl=round(sl, 2), tp=round(tp, 2),
                      reason=reason, time=now_local)
