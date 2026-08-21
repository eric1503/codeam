"""Backtester: uji strategi di data historis SEBELUM pakai uang asli.

Input: CSV candle M5 di <backtest.data_dir>/m5.csv dengan kolom:
    time,open,high,low,close
(time = waktu server broker; export dari MT5: View > Symbols > Bars,
 atau lewat Python: mt5.copy_rates_range)

M15 dan H1 di-resample otomatis dari M5, jadi cukup satu file.

Biaya transaksi (spread + komisi + slippage) DIHITUNG — scalping tanpa
biaya realistis = menipu diri sendiri (lihat docs/04, Jebakan #2).

Keterbatasan yang harus kamu tahu:
  - News filter TIDAK aktif di backtest (tidak ada kalender historis gratis)
    -> hasil live seharusnya sedikit LEBIH BAIK di sisi ini, tapi jangan diandalkan.
  - Kalau SL dan TP tersentuh di candle yang sama, dianggap SL duluan
    (asumsi konservatif / worst case).
"""
import logging
import os
from datetime import timedelta

import numpy as np
import pandas as pd

from ..risk.risk_manager import RiskManager
from ..strategy.mtf_strategy import MTFStrategy

log = logging.getLogger(__name__)

WARMUP_M5 = 3200  # cukup untuk EMA200 H1 (200 jam = 2400 candle M5) + buffer


def _load_m5(data_dir: str) -> pd.DataFrame:
    path = os.path.join(data_dir, "m5.csv")
    if not os.path.exists(path):
        raise FileNotFoundError(
            f"{path} tidak ada. Export data M5 XAUUSD dulu (lihat docstring "
            "backtester.py / docs/04-ROADMAP.md Fase 1)."
        )
    df = pd.read_csv(path)
    df["time"] = pd.to_datetime(df["time"])
    df = df[["time", "open", "high", "low", "close"]].sort_values("time")
    return df.reset_index(drop=True)


def _resample(m5: pd.DataFrame, rule: str) -> pd.DataFrame:
    df = (m5.set_index("time")
            .resample(rule, label="left", closed="left")
            .agg({"open": "first", "high": "max", "low": "min", "close": "last"})
            .dropna()
            .reset_index())
    return df


class Backtester:
    def __init__(self, cfg):
        self.cfg = cfg
        self.bt = cfg.backtest
        self.strategy = MTFStrategy(cfg)
        self.risk = RiskManager(cfg)

    def run(self):
        bt = self.bt
        m5 = _load_m5(bt["data_dir"])
        m15 = _resample(m5, "15min")
        h1 = _resample(m5, "1h")
        log.info("Data: %d candle M5 (%s s/d %s)", len(m5),
                 m5["time"].iat[0], m5["time"].iat[-1])

        balance = float(bt["initial_balance"])
        equity_curve = [balance]
        trades = []
        position = None  # dict: side, entry, sl, tp, lot, time, be_done

        spread = float(bt["spread_usd"])
        slip = float(bt["slippage_usd"])
        comm = float(bt["commission_per_lot"])
        # offset jam: waktu CSV (server broker, umumnya UTC+2/3) -> waktu lokal
        # untuk filter sesi. Default: server UTC+2, lokal WIB UTC+7 -> +5 jam.
        tz_shift = timedelta(hours=int(bt.get("csv_to_local_offset_hours", 5)))

        be_at_r = self.cfg.strategy["breakeven_at_r"]

        for i in range(WARMUP_M5, len(m5)):
            candle = m5.iloc[i]
            t = candle["time"]

            # ---- kelola posisi terbuka di candle ini ----
            if position is not None:
                position, closed = self._manage(position, candle, be_at_r)
                if closed is not None:
                    pnl_raw, exit_reason = closed
                    cost = (spread + slip) * 100.0 * position_lot(position) + \
                           comm * position_lot(position)
                    pnl = pnl_raw - cost
                    balance += pnl
                    self.risk.record_result(pnl, t.date())
                    trades.append({"time_open": position["time"],
                                   "time_close": t, "side": position["side"],
                                   "entry": position["entry"],
                                   "exit_reason": exit_reason,
                                   "lot": position["lot"], "pnl": round(pnl, 2),
                                   "balance": round(balance, 2)})
                    equity_curve.append(balance)
                    position = None

            if position is not None:
                continue  # satu posisi saja (hard rule)

            # ---- cari sinyal pada candle yang baru saja close ----
            m5_closed = m5.iloc[: i + 1]
            close_time = t + timedelta(minutes=5)
            m15_closed = m15[m15["time"] + timedelta(minutes=15) <= close_time]
            h1_closed = h1[h1["time"] + timedelta(hours=1) <= close_time]
            if len(h1_closed) < 210:
                continue

            now_local = (t + timedelta(minutes=5) + tz_shift).to_pydatetime()
            sig = self.strategy.evaluate(h1_closed, m15_closed,
                                         m5_closed.tail(300), now_local)
            if sig is None:
                continue

            ok, why = self.risk.can_open(t.date(), balance, 0, spread)
            if not ok:
                continue
            lot = self.risk.calc_lot(balance, sig.entry, sig.sl)
            if lot <= 0:
                continue
            position = {"side": sig.side, "entry": sig.entry, "sl": sig.sl,
                        "tp": sig.tp, "lot": lot, "time": t,
                        "risk_dist": abs(sig.entry - sig.sl), "be_done": False}

        self._report(trades, equity_curve, balance)
        return trades

    @staticmethod
    def _manage(pos, candle, be_at_r):
        """Simulasi SL/TP (konservatif: SL dicek duluan) + breakeven."""
        lot100 = pos["lot"] * 100.0
        if pos["side"] == "BUY":
            if candle["low"] <= pos["sl"]:
                return pos, ((pos["sl"] - pos["entry"]) * lot100, "SL")
            if candle["high"] >= pos["tp"]:
                return pos, ((pos["tp"] - pos["entry"]) * lot100, "TP")
            if (be_at_r and not pos["be_done"]
                    and candle["high"] >= pos["entry"] + be_at_r * pos["risk_dist"]):
                pos["sl"] = pos["entry"]
                pos["be_done"] = True
        else:
            if candle["high"] >= pos["sl"]:
                return pos, ((pos["entry"] - pos["sl"]) * lot100, "SL")
            if candle["low"] <= pos["tp"]:
                return pos, ((pos["entry"] - pos["tp"]) * lot100, "TP")
            if (be_at_r and not pos["be_done"]
                    and candle["low"] <= pos["entry"] - be_at_r * pos["risk_dist"]):
                pos["sl"] = pos["entry"]
                pos["be_done"] = True
        return pos, None

    def _report(self, trades, equity_curve, balance):
        print("\n" + "=" * 58)
        print("HASIL BACKTEST — XAUUSD MTF Scalper")
        print("=" * 58)
        if not trades:
            print("Tidak ada trade. Cek data / parameter / filter sesi.")
            return
        df = pd.DataFrame(trades)
        wins = df[df["pnl"] > 0]
        losses = df[df["pnl"] <= 0]
        gross_win = wins["pnl"].sum()
        gross_loss = abs(losses["pnl"].sum())
        pf = gross_win / gross_loss if gross_loss > 0 else float("inf")
        eq = pd.Series(equity_curve)
        drawdown = (eq - eq.cummax()) / eq.cummax()
        init = float(self.bt["initial_balance"])

        print(f"Periode          : {df['time_open'].iloc[0]} s/d "
              f"{df['time_close'].iloc[-1]}")
        print(f"Jumlah trade     : {len(df)}")
        print(f"Win rate         : {len(wins) / len(df) * 100:.1f}%")
        print(f"Profit factor    : {pf:.2f}   (target lulus: > 1.3)")
        print(f"Expectancy/trade : {df['pnl'].mean():+.2f} USD")
        print(f"Max drawdown     : {drawdown.min() * 100:.1f}%   "
              f"(target lulus: > -20%)")
        print(f"Balance akhir    : {balance:.2f} USD "
              f"({(balance - init) / init * 100:+.1f}%)")
        print("=" * 58)
        if len(df) < 200:
            print("⚠️  Sampel < 200 trade — belum signifikan secara statistik.")
        out = os.path.join(self.bt["data_dir"], "backtest_trades.csv")
        df.to_csv(out, index=False)
        print(f"Detail per trade tersimpan di: {out}\n")


def position_lot(pos) -> float:
    return pos["lot"]
