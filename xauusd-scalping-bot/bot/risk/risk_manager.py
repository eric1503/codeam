"""Penjaga gerbang risiko. Semua trade harus lolos dari sini.

Aturan yang ditegakkan (lihat docs/03-RISK-MANAGEMENT.md):
  - risk per trade tetap (% dari balance) -> ukuran lot dihitung, bukan ditebak
  - daily loss limit -> berhenti trading sampai besok
  - batas jumlah trade per hari & posisi bersamaan
  - batas spread maksimum saat entry
"""
from datetime import date


class RiskManager:
    def __init__(self, cfg):
        self.cfg = cfg.risk
        self._day: date | None = None
        self._daily_pnl = 0.0
        self._daily_trades = 0

    def _roll_day(self, today: date):
        if self._day != today:
            self._day = today
            self._daily_pnl = 0.0
            self._daily_trades = 0

    def record_result(self, pnl: float, today: date):
        self._roll_day(today)
        self._daily_pnl += pnl
        self._daily_trades += 1

    def can_open(self, today: date, balance: float, open_positions: int,
                 spread_usd: float):
        """Return (boleh_entry: bool, alasan_tolak: str)."""
        self._roll_day(today)
        c = self.cfg
        if balance <= 0:
            return False, "balance tidak valid"
        if self._daily_pnl <= -c["max_daily_loss"] * balance:
            return False, (f"daily loss limit tercapai "
                           f"({self._daily_pnl:+.2f} USD) — berhenti sampai besok")
        if self._daily_trades >= c["max_trades_per_day"]:
            return False, f"batas {c['max_trades_per_day']} trade/hari tercapai"
        if open_positions >= c["max_open_positions"]:
            return False, "sudah ada posisi terbuka"
        if spread_usd > c["max_spread_usd"]:
            return False, f"spread terlalu lebar (${spread_usd:.2f})"
        return True, ""

    def calc_lot(self, balance: float, entry: float, sl: float,
                 contract_size: float = 100.0, min_lot: float = 0.01,
                 lot_step: float = 0.01, max_lot: float = 100.0) -> float:
        """Hitung lot dari risk % dan jarak SL.

        contract_size XAUUSD umumnya 100 oz/lot -> pergerakan $1 harga = $100/lot.
        Return 0.0 kalau risk tidak muat di lot minimum (trade harus di-skip,
        BUKAN dipaksa dengan risk lebih besar).
        """
        risk_money = balance * self.cfg["risk_per_trade"]
        sl_dist = abs(entry - sl)
        if sl_dist <= 0:
            return 0.0
        lot = risk_money / (sl_dist * contract_size)
        lot = int(lot / lot_step) * lot_step  # bulatkan KE BAWAH ke step broker
        if lot < min_lot:
            return 0.0
        return round(min(lot, max_lot), 2)

    @property
    def daily_pnl(self) -> float:
        return self._daily_pnl

    @property
    def daily_trades(self) -> int:
        return self._daily_trades
