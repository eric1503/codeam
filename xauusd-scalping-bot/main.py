"""XAUUSD MTF Scalping Bot — entry point.

Mode:
  python main.py --mode backtest   # uji strategi di data historis (WAJIB duluan)
  python main.py --mode signal     # kirim sinyal ke Telegram, TANPA eksekusi
  python main.py --mode live       # eksekusi otomatis ke MT5 (setelah lulus demo!)
"""
import argparse
import csv
import logging
import os
import time
from datetime import datetime, timezone
from zoneinfo import ZoneInfo

from bot.config import load_config
from bot.news.news_filter import NewsFilter
from bot.risk.risk_manager import RiskManager
from bot.strategy.mtf_strategy import MTFStrategy
from bot.telegram.notifier import TelegramNotifier

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s %(levelname)-7s %(name)s | %(message)s",
)
log = logging.getLogger("main")


def build_feed(cfg):
    provider = cfg.data["provider"]
    if provider == "mt5":
        from bot.data.mt5_feed import MT5Feed
        return MT5Feed(cfg)
    if provider == "twelvedata":
        from bot.data.twelvedata_feed import TwelveDataFeed
        return TwelveDataFeed(cfg)
    raise ValueError(f"data.provider tidak dikenal: {provider}")


def log_trade_csv(path, row: dict):
    exists = os.path.exists(path)
    with open(path, "a", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=list(row))
        if not exists:
            writer.writeheader()
        writer.writerow(row)


def run_live(cfg, execute: bool):
    """Loop utama untuk mode signal (execute=False) dan live (execute=True)."""
    tz = ZoneInfo(cfg.timezone)
    feed = build_feed(cfg)
    feed.connect()
    strategy = MTFStrategy(cfg)
    risk = RiskManager(cfg)
    news = NewsFilter(cfg)
    tg = TelegramNotifier(cfg)

    executor = None
    if execute:
        from bot.execution.mt5_executor import MT5Executor
        executor = MT5Executor(cfg)

    spec = feed.symbol_spec()
    mode_name = "LIVE" if execute else "SIGNAL"
    tg.send(f"🤖 Robot XAUUSD MTF Scalper aktif — mode <b>{mode_name}</b>")
    log.info("Robot jalan (mode %s). Ctrl+C untuk berhenti.", mode_name)

    last_m5_time = None
    last_day = None
    news_warned_for = None
    tracked = {}  # ticket -> info posisi robot (untuk deteksi close & breakeven)

    while True:
        try:
            now_local = datetime.now(tz)
            now_utc = datetime.now(timezone.utc)

            # ---- rekap harian saat ganti hari ----
            if last_day and now_local.date() != last_day:
                tg.daily_summary(risk.daily_trades, risk.daily_pnl,
                                 feed.balance())
            last_day = now_local.date()

            # ---- kelola posisi terbuka (live): breakeven + deteksi close ----
            if executor:
                positions = {p.ticket: p for p in executor.open_positions()}
                for ticket in list(tracked):
                    if ticket not in positions:  # posisi sudah tertutup
                        info = tracked.pop(ticket)
                        pnl = executor.closed_position_pnl(ticket)
                        if pnl is not None:
                            risk.record_result(pnl, now_local.date())
                            tg.trade_closed(info["side"], pnl, "SL/TP")
                            log_trade_csv(cfg.logging["trades_csv"], {
                                "time": now_local.isoformat(), "event": "close",
                                "side": info["side"], "pnl": round(pnl, 2)})
                be_r = cfg.strategy["breakeven_at_r"]
                if be_r:
                    for ticket, p in positions.items():
                        info = tracked.get(ticket)
                        if not info or info.get("be_done"):
                            continue
                        bid, ask, _ = feed.tick()
                        price = bid if info["side"] == "BUY" else ask
                        moved = (price - info["entry"] if info["side"] == "BUY"
                                 else info["entry"] - price)
                        if moved >= be_r * info["risk_dist"]:
                            if executor.move_sl_to_breakeven(p, info["entry"]):
                                info["be_done"] = True
                                tg.send(f"🔒 SL dipindah ke breakeven "
                                        f"({info['entry']:.2f})")

            # ---- tunggu candle M5 baru yang sudah close ----
            m5 = feed.candles("M5", 300)
            if last_m5_time is not None and m5["time"].iat[-1] == last_m5_time:
                time.sleep(cfg.data["poll_seconds"])
                continue
            last_m5_time = m5["time"].iat[-1]

            # ---- filter news ----
            ev = news.blocking_event(now_utc)
            if ev:
                if news_warned_for != ev["title"]:
                    news_warned_for = ev["title"]
                    tg.warn(f"News filter aktif: <b>{ev['title']}</b> "
                            f"({ev['impact']}) — robot tidak entry sementara.")
                    if (executor and
                            cfg.news["close_positions_before_news"]):
                        for p in executor.open_positions():
                            executor.close_position(p, "news")
                        tg.warn("Semua posisi ditutup sebelum news.")
                time.sleep(cfg.data["poll_seconds"])
                continue
            news_warned_for = None

            # ---- evaluasi strategi ----
            m15 = feed.candles("M15", 300)
            h1 = feed.candles("H1", 300)
            sig = strategy.evaluate(h1, m15, m5, now_local)
            if sig is None:
                time.sleep(cfg.data["poll_seconds"])
                continue

            # ---- gerbang risiko ----
            bid, ask, spread = feed.tick()
            open_count = len(executor.open_positions()) if executor else 0
            balance = feed.balance() or 1000.0  # mode sinyal tanpa akun: nominal
            ok, why = risk.can_open(now_local.date(), balance, open_count,
                                    spread)
            if not ok:
                log.info("Sinyal %s DITOLAK risk manager: %s", sig.side, why)
                time.sleep(cfg.data["poll_seconds"])
                continue
            lot = risk.calc_lot(balance, sig.entry, sig.sl,
                                contract_size=spec["contract_size"],
                                min_lot=spec["min_lot"],
                                lot_step=spec["lot_step"],
                                max_lot=spec["max_lot"])
            if lot <= 0:
                log.info("Sinyal di-skip: risk tidak muat di lot minimum "
                         "(jarak SL terlalu jauh untuk balance saat ini).")
                time.sleep(cfg.data["poll_seconds"])
                continue

            # ---- kirim sinyal / eksekusi ----
            tg.signal(sig, lot, mode_name)
            log_trade_csv(cfg.logging["trades_csv"], {
                "time": now_local.isoformat(), "event": "signal",
                "side": sig.side, "entry": sig.entry, "sl": sig.sl,
                "tp": sig.tp, "lot": lot, "reason": sig.reason})
            if executor:
                result = executor.market_order(sig.side, lot, sig.sl, sig.tp)
                if result:
                    tracked[result.order] = {
                        "side": sig.side, "entry": sig.entry,
                        "risk_dist": abs(sig.entry - sig.sl), "be_done": False}
                else:
                    tg.warn("Eksekusi order GAGAL — cek terminal MT5!")

            time.sleep(cfg.data["poll_seconds"])

        except KeyboardInterrupt:
            log.info("Dihentikan oleh user.")
            tg.send("🛑 Robot dimatikan manual.")
            break
        except Exception as e:
            log.exception("Error di loop utama: %s", e)
            tg.warn(f"Robot error: {e} — retry 60 detik lagi.")
            time.sleep(60)

    feed.shutdown()


def main():
    parser = argparse.ArgumentParser(description="XAUUSD MTF Scalping Bot")
    parser.add_argument("--mode", choices=["backtest", "signal", "live"],
                        required=True)
    parser.add_argument("--config", default="config.yaml")
    args = parser.parse_args()

    cfg = load_config(args.config)

    if args.mode == "backtest":
        from bot.backtest.backtester import Backtester
        Backtester(cfg).run()
    elif args.mode == "signal":
        run_live(cfg, execute=False)
    else:
        confirm = input(
            "⚠️  MODE LIVE: robot akan mengeksekusi order sungguhan di akun "
            "MT5 yang sedang login.\nSudah lulus backtest + minimal 3 bulan "
            "demo? Ketik 'YA SAYA PAHAM' untuk lanjut: "
        )
        if confirm.strip() != "YA SAYA PAHAM":
            print("Dibatalkan. Mulai dari --mode backtest / --mode signal dulu.")
            return
        run_live(cfg, execute=True)


if __name__ == "__main__":
    main()
