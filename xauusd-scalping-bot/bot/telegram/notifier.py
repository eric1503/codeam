"""Notifikasi Telegram via Bot API (gratis — token dari @BotFather).

Endpoint yang dipakai cuma satu:
    https://api.telegram.org/bot<TOKEN>/sendMessage
"""
import logging

import requests

log = logging.getLogger(__name__)


class TelegramNotifier:
    def __init__(self, cfg):
        self.cfg = cfg.telegram
        self.enabled = bool(self.cfg["enabled"] and self.cfg["bot_token"]
                            and self.cfg["chat_id"])
        if self.cfg["enabled"] and not self.enabled:
            log.warning("Telegram dinyalakan tapi bot_token/chat_id kosong "
                        "di config.yaml — notifikasi dimatikan.")

    def send(self, text: str):
        if not self.enabled:
            log.info("[TELEGRAM-OFF] %s", text)
            return
        url = f"https://api.telegram.org/bot{self.cfg['bot_token']}/sendMessage"
        try:
            resp = requests.post(
                url,
                json={"chat_id": self.cfg["chat_id"], "text": text,
                      "parse_mode": "HTML"},
                timeout=10,
            )
            if resp.status_code != 200:
                log.warning("Telegram error %s: %s", resp.status_code, resp.text)
        except requests.RequestException as e:
            log.warning("Telegram gagal terkirim: %s", e)

    # ---------- Pesan terformat ----------

    def signal(self, sig, lot: float, mode: str):
        arrow = "🟢 BUY" if sig.side == "BUY" else "🔴 SELL"
        self.send(
            f"{arrow} <b>XAUUSD</b> [{mode}]\n"
            f"Entry : <code>{sig.entry:.2f}</code>\n"
            f"SL    : <code>{sig.sl:.2f}</code>\n"
            f"TP    : <code>{sig.tp:.2f}</code>\n"
            f"Lot   : <code>{lot}</code>\n"
            f"🧠 {sig.reason}"
        )

    def trade_closed(self, side: str, pnl: float, reason: str):
        emoji = "✅" if pnl >= 0 else "❌"
        self.send(f"{emoji} Posisi {side} ditutup ({reason}) — "
                  f"P/L: <b>{pnl:+.2f} USD</b>")

    def daily_summary(self, trades: int, pnl: float, balance: float):
        self.send(
            "📊 <b>Rekap Harian</b>\n"
            f"Jumlah trade : {trades}\n"
            f"P/L hari ini : {pnl:+.2f} USD\n"
            f"Balance      : {balance:.2f} USD"
        )

    def warn(self, text: str):
        self.send(f"⚠️ {text}")
