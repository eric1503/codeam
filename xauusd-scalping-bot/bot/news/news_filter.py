"""Filter news / kalender ekonomi.

Sumber: JSON mingguan Forex Factory (gratis, tanpa API key):
    https://nfs.faireconomy.media/ff_calendar_thisweek.json

Format tiap event:
    {"title": "FOMC Statement", "country": "USD",
     "date": "2026-08-20T14:00:00-04:00", "impact": "High",
     "forecast": "...", "previous": "..."}

Robot TIDAK menebak arah news — robot MENGHINDAR: tidak entry di jendela
[before, after] menit sekitar event high-impact. Lihat docs/01 bagian C.
"""
import logging
from datetime import datetime, timedelta, timezone

import requests

log = logging.getLogger(__name__)

FF_CALENDAR_URL = "https://nfs.faireconomy.media/ff_calendar_thisweek.json"


class NewsFilter:
    def __init__(self, cfg):
        self.cfg = cfg.news
        self._events: list[dict] = []
        self._fetched_at: datetime | None = None

    def _refresh(self, now_utc: datetime):
        """Ambil ulang kalender tiap 4 jam."""
        if self._fetched_at and now_utc - self._fetched_at < timedelta(hours=4):
            return
        try:
            resp = requests.get(FF_CALENDAR_URL, timeout=15)
            resp.raise_for_status()
            raw = resp.json()
        except Exception as e:  # jaringan gagal -> pakai cache lama
            log.warning("Gagal ambil kalender ekonomi: %s", e)
            if self._fetched_at is None:
                self._events = []
            return
        events = []
        for ev in raw:
            if ev.get("country") not in self.cfg["currencies"]:
                continue
            if ev.get("impact") not in self.cfg["impact_levels"]:
                continue
            try:
                when = datetime.fromisoformat(ev["date"]).astimezone(timezone.utc)
            except (KeyError, ValueError):
                continue
            events.append({"title": ev.get("title", "?"), "time": when,
                           "impact": ev.get("impact")})
        self._events = events
        self._fetched_at = now_utc
        log.info("Kalender ekonomi dimuat: %d event terfilter minggu ini",
                 len(events))

    def blocking_event(self, now_utc: datetime):
        """Return event yang sedang memblokir trading, atau None."""
        if not self.cfg["enabled"]:
            return None
        self._refresh(now_utc)
        before = timedelta(minutes=self.cfg["block_minutes_before"])
        after = timedelta(minutes=self.cfg["block_minutes_after"])
        for ev in self._events:
            if ev["time"] - before <= now_utc <= ev["time"] + after:
                return ev
        return None

    def upcoming(self, now_utc: datetime, within_hours: int = 24) -> list[dict]:
        """Event yang akan datang (untuk laporan harian ke Telegram)."""
        self._refresh(now_utc)
        horizon = now_utc + timedelta(hours=within_hours)
        return [ev for ev in self._events if now_utc <= ev["time"] <= horizon]
