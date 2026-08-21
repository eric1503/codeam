"""Eksekusi order ke MetaTrader 5.

Semua order SELALU dikirim dengan SL & TP terpasang (hard rule #1).
Magic number menandai order milik robot ini, supaya tidak mengganggu
posisi manual kamu di akun yang sama.
"""
import logging

log = logging.getLogger(__name__)

try:
    import MetaTrader5 as mt5
except ImportError:
    mt5 = None

MAGIC = 51015  # penanda order robot (H1->M15->M5 :)


class MT5Executor:
    def __init__(self, cfg):
        if mt5 is None:
            raise RuntimeError("MetaTrader5 tidak tersedia — mode live butuh "
                               "Windows + package MetaTrader5.")
        self.symbol = cfg.symbol

    def open_positions(self):
        """Posisi terbuka milik robot ini saja (filter via magic number)."""
        positions = mt5.positions_get(symbol=self.symbol) or []
        return [p for p in positions if p.magic == MAGIC]

    def market_order(self, side: str, lot: float, sl: float, tp: float,
                     comment: str = "mtf-scalper"):
        tick = mt5.symbol_info_tick(self.symbol)
        if side == "BUY":
            order_type, price = mt5.ORDER_TYPE_BUY, tick.ask
        else:
            order_type, price = mt5.ORDER_TYPE_SELL, tick.bid
        request = {
            "action": mt5.TRADE_ACTION_DEAL,
            "symbol": self.symbol,
            "volume": lot,
            "type": order_type,
            "price": price,
            "sl": sl,
            "tp": tp,
            "deviation": 20,          # toleransi slippage (points)
            "magic": MAGIC,
            "comment": comment,
            "type_time": mt5.ORDER_TIME_GTC,
            "type_filling": mt5.ORDER_FILLING_IOC,
        }
        result = mt5.order_send(request)
        if result is None or result.retcode != mt5.TRADE_RETCODE_DONE:
            code = result.retcode if result else mt5.last_error()
            log.error("Order gagal (%s): %s", side, code)
            return None
        log.info("Order %s %.2f lot @ %.2f (SL %.2f / TP %.2f) — ticket %s",
                 side, lot, price, sl, tp, result.order)
        return result

    def move_sl_to_breakeven(self, position, entry_price: float):
        """Geser SL ke harga entry (dipanggil setelah profit >= 1R)."""
        request = {
            "action": mt5.TRADE_ACTION_SLTP,
            "symbol": self.symbol,
            "position": position.ticket,
            "sl": entry_price,
            "tp": position.tp,
        }
        result = mt5.order_send(request)
        ok = result and result.retcode == mt5.TRADE_RETCODE_DONE
        if ok:
            log.info("SL posisi %s dipindah ke breakeven %.2f",
                     position.ticket, entry_price)
        return ok

    def closed_position_pnl(self, ticket: int):
        """Total P/L (profit + komisi + swap) sebuah posisi yang sudah tertutup,
        dibaca dari history deals. Return None kalau belum ada di history."""
        deals = mt5.history_deals_get(position=ticket)
        if not deals:
            return None
        return sum(d.profit + d.commission + d.swap for d in deals)

    def close_position(self, position, reason: str = "manual"):
        tick = mt5.symbol_info_tick(self.symbol)
        if position.type == mt5.POSITION_TYPE_BUY:
            order_type, price = mt5.ORDER_TYPE_SELL, tick.bid
        else:
            order_type, price = mt5.ORDER_TYPE_BUY, tick.ask
        request = {
            "action": mt5.TRADE_ACTION_DEAL,
            "symbol": self.symbol,
            "volume": position.volume,
            "type": order_type,
            "position": position.ticket,
            "price": price,
            "deviation": 20,
            "magic": MAGIC,
            "comment": f"close:{reason}",
            "type_time": mt5.ORDER_TIME_GTC,
            "type_filling": mt5.ORDER_FILLING_IOC,
        }
        result = mt5.order_send(request)
        return result and result.retcode == mt5.TRADE_RETCODE_DONE
