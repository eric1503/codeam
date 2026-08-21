# 01 — Panduan Lengkap Semua API yang Dibutuhkan

Ini jawaban lengkap untuk kendala kamu waktu bikin di ChatGPT: **ya, harga real-time
butuh sumber data (API atau koneksi broker)**, dan **ya, Telegram juga butuh API**
(tapi dua-duanya bisa gratis). Berikut semua opsinya, dari yang paling direkomendasikan.

---

## A. API Harga Real-Time XAUUSD

### ⭐ Opsi 1 (REKOMENDASI): MetaTrader 5 Python — GRATIS & real-time tick

Ini cara yang dipakai mayoritas pembuat robot trading retail di seluruh dunia
(termasuk komunitas trader algo Indonesia). Kamu **tidak bayar API sama sekali** —
harga real-time datang dari broker kamu sendiri lewat terminal MT5.

**Cara setup:**
1. Buka akun **demo** di broker yang menyediakan XAUUSD dan platform MT5:
   - Populer di Indonesia: Exness, FBS, XM, OctaFX, HFM
   - Populer global (spread ketat, bagus untuk scalping): IC Markets, Pepperstone, Tickmill
   - ⚠️ Untuk scalping XAUUSD, **spread dan komisi sangat menentukan**. Cari akun
     tipe "Raw/Zero/ECN" — spread gold bisa 5–15 cent vs 30–50 cent di akun standard.
     Scalping dengan target 20–50 pip gold, spread 35 cent = langsung minus 10–20% dari target.
2. Install terminal MetaTrader 5 (Windows) dan login.
3. `pip install MetaTrader5`
4. Dari Python:

```python
import MetaTrader5 as mt5

mt5.initialize()                      # konek ke terminal MT5 yang sedang jalan
tick = mt5.symbol_info_tick("XAUUSD") # harga real-time saat ini
print(tick.bid, tick.ask)

# Ambil 500 candle M5 terakhir:
rates = mt5.copy_rates_from_pos("XAUUSD", mt5.TIMEFRAME_M5, 0, 500)
```

**Kelebihan:** gratis, tick-level real-time, sekaligus bisa eksekusi order dari Python.
**Kekurangan:** butuh Windows (solusi: VPS Windows murah ±Rp 70–150rb/bln — ini
standar untuk robot yang jalan 24 jam, sekalian internet stabil).

> Catatan: nama simbol beda-beda per broker: `XAUUSD`, `XAUUSDm`, `XAUUSD.a`, `GOLD`.
> Cek di Market Watch MT5 kamu, lalu sesuaikan di `config.yaml`.

### Opsi 2: Twelve Data — REST + WebSocket

- Website: https://twelvedata.com
- Free tier: ±800 credits/hari, 8 request/menit — cukup untuk polling M5.
- Support simbol `XAU/USD`, ada endpoint `time_series` (candle OHLC) dan `price`.
- WebSocket real-time butuh plan berbayar (mulai ±$29/bln).

```
GET https://api.twelvedata.com/time_series?symbol=XAU/USD&interval=5min&outputsize=500&apikey=API_KEY_KAMU
```

### Opsi 3: OANDA v20 REST API

- https://developer.oanda.com — akun demo (practice) gratis, dapat API token.
- Instrumen `XAU_USD`, ada streaming harga real-time gratis untuk pemegang akun.
- Bagus kalau mau serverless/Linux tanpa MT5. Python: `pip install oandapyV20`.

### Opsi 4: Lainnya (pelengkap)

| Layanan | Gratis? | Catatan |
|---|---|---|
| GoldAPI.io | 100 req/bln gratis | Spot gold saja, terlalu sedikit untuk robot |
| Finnhub | Ya (terbatas) | Forex/gold di free tier terbatas; bagus untuk kalender ekonomi |
| Alpha Vantage | 25 req/hari | Terlalu sedikit untuk scalping |
| Polygon.io | Berbayar untuk forex real-time | Kualitas bagus |
| Yahoo Finance (`yfinance`) | Gratis | `GC=F` (futures), delay & tidak untuk live — cukup untuk backtest kasar |

**Kesimpulan:** pakai **MT5 (Opsi 1)**. Gratis, real-time, dan langsung bisa eksekusi
order. Robot di repo ini sudah mendukung MT5 sebagai feed utama dan Twelve Data
sebagai alternatif.

---

## B. API Telegram (untuk kirim sinyal & laporan)

**Ya, butuh API — tapi 100% gratis dan setup-nya 5 menit:**

1. Buka Telegram, chat **@BotFather** → kirim `/newbot` → kasih nama → BotFather
   kasih **token** seperti `123456789:AAHfj3k2...`. Simpan baik-baik (ini rahasia!).
2. Cari **chat_id** kamu: chat **@userinfobot** → dia balas dengan ID kamu
   (misal `5512345678`). Atau untuk grup: masukkan bot ke grup, lalu buka
   `https://api.telegram.org/bot<TOKEN>/getUpdates` dan lihat `chat.id` (grup biasanya negatif).
3. Kirim pesan cukup dengan HTTP request biasa (tanpa library pun bisa):

```
https://api.telegram.org/bot<TOKEN>/sendMessage?chat_id=<CHAT_ID>&text=Halo
```

Robot ini (`bot/telegram/notifier.py`) memakai endpoint itu untuk mengirim:
- 🔔 Sinyal entry (arah, harga, SL, TP, lot, alasan sinyal)
- ✅/❌ Hasil trade (TP kena / SL kena, profit/loss)
- 📊 Rekap harian (jumlah trade, win rate, P/L)
- ⛔ Peringatan (daily loss limit tercapai, news filter aktif, koneksi putus)

---

## C. API Kalender Ekonomi & News (FOMC, NFP, CPI, dll)

Untuk gold, news yang paling menggerakkan harga (urutan dampak):

1. **FOMC** (keputusan suku bunga The Fed + konferensi pers Powell) — dampak terbesar
2. **NFP** (Non-Farm Payrolls, Jumat pertama tiap bulan, 19:30/20:30 WIB)
3. **CPI** AS (inflasi)
4. **PCE**, GDP AS, PPI, Retail Sales, Jobless Claims
5. Pidato pejabat The Fed, situasi geopolitik (perang → gold naik)

### Sumber kalender ekonomi (dipakai `bot/news/news_filter.py`):

| Sumber | Gratis? | Cara |
|---|---|---|
| ⭐ Forex Factory weekly JSON | Ya | `https://nfs.faireconomy.media/ff_calendar_thisweek.json` — JSON resmi berisi event seminggu + level dampak (High/Medium/Low). Robot ini pakai ini. |
| Finnhub economic calendar | Ya (free tier) | `GET /calendar/economic` |
| Trading Economics API | Trial/berbayar | Paling lengkap, kelas institusi |
| investing.com | Scraping (rapuh) | Tidak direkomendasikan untuk robot |

### Bagaimana robot "menganalisa" news?

Jujur dan penting dipahami — ada 2 level:

**Level 1 — News FILTER (yang diimplementasikan robot ini, dan yang dipakai
mayoritas robot retail yang bertahan lama):**
Robot TIDAK menebak arah news. Robot **berhenti trading X menit sebelum & sesudah
event high-impact** dan (opsional) menutup posisi terbuka sebelum event. Kenapa?
- Saat FOMC/NFP, spread XAUUSD melebar 5–20x lipat dan harga bisa loncat 100–300 pip
  dalam 1 detik (slippage). SL kamu bisa kena di harga jauh lebih buruk.
- Statistik komunitas algo: mayoritas kematian robot scalping terjadi saat news.
- "Tidak trading saat news" adalah edge tersendiri.

**Level 2 — News TRADING / analisa sentimen (arah masa depan project ini):**
Membaca angka aktual vs forecast (misal CPI aktual > forecast → USD menguat → gold
cenderung turun) lalu entry searah. Ini bisa ditambahkan nanti membaca field
`actual` vs `forecast` dari JSON Forex Factory — tapi butuh eksekusi super cepat dan
spread saat itu buruk. Analisa sentimen headline dengan AI/LLM juga mungkin, tapi
itu tahap lanjut setelah robot dasarnya terbukti profit. Jangan mulai dari sini.

---

## D. Ringkasan: Yang Harus Kamu Siapkan

- [ ] Akun **demo** MT5 di broker (gratis) → login, password, server
- [ ] VPS Windows kalau mau jalan 24 jam (opsional di awal, bisa PC sendiri dulu)
- [ ] Token bot Telegram dari @BotFather + chat_id kamu
- [ ] (Opsional) API key Twelve Data kalau tidak pakai MT5
- [ ] Isi semua ke `config.yaml`
- [ ] JANGAN pernah commit/share token & password ke GitHub (file `config.yaml`
      sengaja tidak di-commit, hanya `config.example.yaml`)
