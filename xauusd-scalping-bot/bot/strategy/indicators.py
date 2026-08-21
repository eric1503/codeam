"""Indikator teknikal murni pandas/numpy (tanpa library TA eksternal).

Semua fungsi menerima DataFrame candle dengan kolom:
    time (datetime), open, high, low, close
"""
import numpy as np
import pandas as pd


def ema(series: pd.Series, period: int) -> pd.Series:
    return series.ewm(span=period, adjust=False).mean()


def rsi(series: pd.Series, period: int = 14) -> pd.Series:
    delta = series.diff()
    gain = delta.clip(lower=0).ewm(alpha=1 / period, adjust=False).mean()
    loss = (-delta.clip(upper=0)).ewm(alpha=1 / period, adjust=False).mean()
    rs = gain / loss.replace(0, np.nan)
    return (100 - 100 / (1 + rs)).fillna(50.0)


def atr(df: pd.DataFrame, period: int = 14) -> pd.Series:
    prev_close = df["close"].shift(1)
    tr = pd.concat(
        [
            df["high"] - df["low"],
            (df["high"] - prev_close).abs(),
            (df["low"] - prev_close).abs(),
        ],
        axis=1,
    ).max(axis=1)
    return tr.ewm(alpha=1 / period, adjust=False).mean()


def swing_points(df: pd.DataFrame, lookback: int = 2):
    """Deteksi swing high/low ala fractal: candle dengan `lookback` candle
    lebih rendah/tinggi di kiri DAN kanannya.

    Return: (swing_highs, swing_lows) — list of (index, price).
    Candle `lookback` terakhir belum bisa dikonfirmasi (belum ada kanan-nya).
    """
    highs, lows = [], []
    h, l = df["high"].values, df["low"].values
    for i in range(lookback, len(df) - lookback):
        window_h = h[i - lookback : i + lookback + 1]
        window_l = l[i - lookback : i + lookback + 1]
        if h[i] == window_h.max() and (window_h == h[i]).sum() == 1:
            highs.append((i, h[i]))
        if l[i] == window_l.min() and (window_l == l[i]).sum() == 1:
            lows.append((i, l[i]))
    return highs, lows


def structure_bias(df: pd.DataFrame, lookback: int = 2) -> str:
    """Baca struktur market dari 2 swing high & 2 swing low terakhir.

    HH+HL -> "bullish", LH+LL -> "bearish", selain itu "neutral".
    """
    highs, lows = swing_points(df, lookback)
    if len(highs) < 2 or len(lows) < 2:
        return "neutral"
    hh = highs[-1][1] > highs[-2][1]
    hl = lows[-1][1] > lows[-2][1]
    lh = highs[-1][1] < highs[-2][1]
    ll = lows[-1][1] < lows[-2][1]
    if hh and hl:
        return "bullish"
    if lh and ll:
        return "bearish"
    return "neutral"


# ---------- Pola candle (dipakai sebagai trigger entry di M5) ----------

def _body(o, c):
    return abs(c - o)


def is_bullish_engulfing(df: pd.DataFrame, i: int) -> bool:
    if i < 1:
        return False
    o1, c1 = df["open"].iat[i - 1], df["close"].iat[i - 1]
    o2, c2 = df["open"].iat[i], df["close"].iat[i]
    return c1 < o1 and c2 > o2 and c2 >= o1 and o2 <= c1 and _body(o2, c2) > _body(o1, c1)


def is_bearish_engulfing(df: pd.DataFrame, i: int) -> bool:
    if i < 1:
        return False
    o1, c1 = df["open"].iat[i - 1], df["close"].iat[i - 1]
    o2, c2 = df["open"].iat[i], df["close"].iat[i]
    return c1 > o1 and c2 < o2 and c2 <= o1 and o2 >= c1 and _body(o2, c2) > _body(o1, c1)


def is_bullish_pinbar(df: pd.DataFrame, i: int, wick_ratio: float = 2.0) -> bool:
    """Hammer: ekor bawah panjang >= wick_ratio x body, ekor atas kecil."""
    o, h, l, c = (df[k].iat[i] for k in ("open", "high", "low", "close"))
    body = max(_body(o, c), 1e-9)
    lower_wick = min(o, c) - l
    upper_wick = h - max(o, c)
    return lower_wick >= wick_ratio * body and upper_wick <= body


def is_bearish_pinbar(df: pd.DataFrame, i: int, wick_ratio: float = 2.0) -> bool:
    """Shooting star: ekor atas panjang >= wick_ratio x body, ekor bawah kecil."""
    o, h, l, c = (df[k].iat[i] for k in ("open", "high", "low", "close"))
    body = max(_body(o, c), 1e-9)
    lower_wick = min(o, c) - l
    upper_wick = h - max(o, c)
    return upper_wick >= wick_ratio * body and lower_wick <= body
