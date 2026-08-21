# 02 — Strategi Multi-Timeframe H1 → M15 → M5 (Cara Kerja Otak Robot)

Strategi robot ini meniru cara trading manual kamu, diterjemahkan jadi aturan yang
bisa dihitung komputer. Semua logika ada di `bot/strategy/mtf_strategy.py`.

## Filosofi

> "Trade dengan trend timeframe besar, entry presisi di timeframe kecil."

Ini pendekatan yang sama dengan yang diajarkan trader-trader kompeten dunia
(konsep top-down analysis / multi-timeframe confluence — dipopulerkan antara lain
oleh Alexander Elder dengan "Triple Screen Trading System" di buku
*Trading for a Living*, dan dipakai luas di komunitas ICT/SMC maupun price action
klasik ala Al Brooks & Bob Volman untuk scalping).

## Langkah 1 — H1: Tentukan Trend (BOLEH-nya arah apa)

Robot menilai trend H1 dengan 2 syarat yang harus sepakat:

1. **EMA 50 vs EMA 200** (arah rata-rata):
   - EMA50 > EMA200 dan harga di atas EMA50 → bias **BULLISH**
   - EMA50 < EMA200 dan harga di bawah EMA50 → bias **BEARISH**
2. **Struktur market** (higher highs/lows vs lower highs/lows) dari deteksi
   swing point otomatis:
   - HH + HL beruntun → konfirmasi bullish
   - LH + LL beruntun → konfirmasi bearish

Kalau keduanya tidak sepakat → **NETRAL → robot tidak trading**. Diam adalah posisi.

## Langkah 2 — M15: Gambar Level (DI MANA boleh entry)

Seperti kamu menggambar chart di M15, robot otomatis:

1. Deteksi **swing high & swing low** M15 (fractal 5-candle).
2. Bangun **zona support/resistance** dari swing point yang teruji (disentuh berkali-kali).
3. Hitung **pullback**: dalam trend bullish, tunggu harga turun ke zona demand /
   area value (antara EMA20–EMA50 M15 atau zona support terdekat). Dalam trend
   bearish sebaliknya.

Robot hanya menyalakan "lampu kuning" (siap entry) kalau harga **masuk zona** yang
searah trend H1. Tidak kejar harga di tengah-tengah (no chasing).

## Langkah 3 — M5: Trigger Entry (KAPAN tepatnya masuk)

Saat lampu kuning menyala, robot menunggu candle konfirmasi di M5:

- **Bullish engulfing** atau **pin bar/hammer** (rejection dari zona) untuk BUY
- **Bearish engulfing** atau **shooting star** untuk SELL
- Filter tambahan: RSI(14) M5 tidak boleh sudah overbought (>70) saat mau BUY
  atau oversold (<30) saat mau SELL — mencegah entry telat.
- Filter sesi: default hanya trading **sesi London & New York** (14:00–23:00 WIB),
  karena di sesi Asia gold sering flat/choppy dan spread relatif lebih besar
  dibanding pergerakannya.

## Penempatan SL & TP

- **SL**: di bawah swing low M5 terakhir (BUY) / di atas swing high (SELL),
  ditambah buffer `0.3 × ATR(14) M5`. ATR dipakai supaya SL menyesuaikan volatilitas
  — saat gold liar, SL otomatis lebih longgar; saat tenang, lebih ketat.
- **SL minimum**: dibatasi minimal `1.0 × ATR` — SL terlalu ketat = mati kena noise.
- **TP**: `RR × jarak SL` (default RR = 2.0, bisa diatur di config).
- **(Opsional) Breakeven**: setelah profit berjalan 1R, SL dipindah ke harga entry.
- **(Opsional) Trailing stop**: trail sejauh 1×ATR setelah 1.5R.

## Kenapa Aturan Ini? (Riset dari Trader Kompeten)

Ringkasan konsensus dari sumber-sumber yang paling dihormati di dunia trading
(detail RR & sizing di [03-RISK-MANAGEMENT.md](03-RISK-MANAGEMENT.md)):

- **Trend-following multi-timeframe** — Alexander Elder (Triple Screen): timeframe
  besar menentukan arah, timeframe kecil menentukan timing. Terbukti mengurangi
  entry melawan arus.
- **Trading pullback, bukan breakout kejar harga** — Al Brooks (*Trading Price
  Action Trends*): probabilitas lebih tinggi masuk saat harga "diskon" dalam trend.
- **ATR untuk stop** — Chuck LeBeau & konsep Chandelier Exit; Van Tharp juga
  memakai volatilitas untuk sizing. SL statis (misal selalu 20 pip) buruk untuk
  gold karena volatilitasnya berubah-ubah drastis.
- **Session filter** — riset umum komunitas scalper gold (luar & Indonesia):
  mayoritas pergerakan searah XAUUSD terjadi di overlap London–NY.
- **News filter** — pembunuh #1 robot scalping adalah spread melebar + slippage
  saat news besar (FOMC/NFP). Lihat [01-PANDUAN-API.md](01-PANDUAN-API.md) bagian C.

## Kondisi Robot TIDAK Trading (sama pentingnya dengan kapan entry)

- Trend H1 netral / EMA dan struktur tidak sepakat
- Di luar sesi London/NY
- ±60 menit sekitar news high-impact USD
- Daily loss limit sudah tercapai (default -2%)
- Jumlah trade harian maksimal tercapai (default 5)
- Sudah ada posisi terbuka (default 1 posisi saja)
- Spread saat itu > batas maksimum di config (proteksi spread melebar)
- Hari Jumat malam menjelang market tutup (weekend gap risk)

## Yang Harus Kamu Sadari

Strategi ini adalah **kerangka yang masuk akal**, bukan mesin uang jadi. Parameter
(periode EMA, RR, buffer ATR, sesi) HARUS kamu kalibrasi lewat backtest dan forward
test — lihat [04-ROADMAP.md](04-ROADMAP.md). Ubah parameter di `config.yaml`,
jangan di kode, supaya eksperimenmu tercatat rapi.
