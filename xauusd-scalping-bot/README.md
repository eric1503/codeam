# 🥇 XAUUSD Scalping Bot — Multi-Timeframe (H1 → M15 → M5)

Robot trading XAUUSD (Gold) dengan gaya trading: **cek trend di H1, mapping struktur di M15, entry di M5** — persis seperti cara trading manual kamu, tapi diotomatisasi.

> ⚠️ **BACA DULU — Ekspektasi Realistis**
>
> Target 5–10% **per hari** secara konsisten itu **tidak realistis** dan justru berbahaya.
> 5%/hari di-compound = ±120.000.000% per tahun. Tidak ada trader, hedge fund, atau robot
> di dunia yang pernah melakukan itu secara konsisten. Sebagai perbandingan:
> - Prop firm terbesar dunia (FTMO, FundedNext, The5ers) menetapkan **max daily LOSS 5%**
>   — artinya 5% sehari dianggap batas kehancuran akun, bukan target profit.
> - Trader profesional yang bagus menghasilkan **5–15% per BULAN**, itu pun tidak setiap bulan.
> - Hedge fund terbaik dunia (Renaissance Medallion) rata-rata ±66%/TAHUN.
>
> Untuk mengejar 5–10%/hari kamu harus risk 10–30% per trade → secara matematis
> (risk of ruin) akunmu hampir pasti habis dalam hitungan minggu.
> Robot ini dibangun dengan target yang benar: **bertahan hidup dulu, profit konsisten kemudian.**
> Detail lengkap ada di [docs/03-RISK-MANAGEMENT.md](docs/03-RISK-MANAGEMENT.md).

---

## 📁 Struktur Project

```
xauusd-scalping-bot/
├── main.py                     # Entry point — jalankan robot dari sini
├── config.example.yaml         # Template konfigurasi (copy jadi config.yaml)
├── requirements.txt
├── docs/
│   ├── 01-PANDUAN-API.md       # SEMUA API yang dibutuhkan (harga real-time, Telegram, news)
│   ├── 02-STRATEGI.md          # Penjelasan strategi H1→M15→M5 secara detail
│   ├── 03-RISK-MANAGEMENT.md   # RR ideal, position sizing, ekspektasi realistis
│   └── 04-ROADMAP.md           # Perjalanan: backtest → demo → live (jalan panjangnya)
└── bot/
    ├── config.py               # Loader konfigurasi
    ├── data/
    │   ├── mt5_feed.py         # Data real-time via MetaTrader 5 (GRATIS, rekomendasi utama)
    │   └── twelvedata_feed.py  # Alternatif: Twelve Data REST API
    ├── strategy/
    │   ├── indicators.py       # EMA, RSI, ATR, swing high/low, engulfing, pin bar
    │   └── mtf_strategy.py     # Otak robot: H1 trend → M15 zone → M5 trigger
    ├── risk/
    │   └── risk_manager.py     # Position sizing, daily loss limit, RR enforcement
    ├── news/
    │   └── news_filter.py      # Blokir trading saat news besar (FOMC, NFP, CPI, dll)
    ├── telegram/
    │   └── notifier.py         # Kirim sinyal & laporan ke Telegram
    ├── execution/
    │   └── mt5_executor.py     # Eksekusi order otomatis ke MetaTrader 5
    └── backtest/
        └── backtester.py       # Uji strategi di data historis SEBELUM pakai uang asli
```

## 🚀 Quick Start

### 1. Install dependencies

```bash
pip install -r requirements.txt
```

> Package `MetaTrader5` hanya jalan di **Windows** (atau VPS Windows / Wine).
> Kalau kamu di Mac/Linux, pakai mode `twelvedata` untuk data, atau sewa VPS Windows
> murah (±Rp 70–150rb/bulan) — ini standar industri untuk robot MT5.

### 2. Siapkan akun & API (detail lengkap di [docs/01-PANDUAN-API.md](docs/01-PANDUAN-API.md))

1. **Broker MT5** — buka akun **DEMO** dulu di broker yang ada XAUUSD
   (Exness, IC Markets, FBS, XM, dll). Gratis, dan kamu dapat harga real-time gratis.
2. **Telegram Bot** — chat [@BotFather](https://t.me/BotFather) → `/newbot` → dapat token. Gratis.
3. **(Opsional) Twelve Data** — daftar di twelvedata.com untuk API key gratis
   (kalau tidak pakai MT5).

### 3. Konfigurasi

```bash
cp config.example.yaml config.yaml
# lalu edit config.yaml — isi token Telegram, login MT5, dll
```

### 4. Backtest dulu (WAJIB!)

```bash
python main.py --mode backtest
```

Jangan pernah jalankan robot dengan uang asli sebelum:
- Backtest minimal 2 tahun data → profit factor > 1.3, max drawdown < 20%
- Forward test di akun DEMO minimal 3 bulan

### 5. Jalankan (mode sinyal — kirim sinyal ke Telegram tanpa eksekusi)

```bash
python main.py --mode signal
```

### 6. Jalankan (mode live — eksekusi otomatis ke MT5)

```bash
python main.py --mode live
```

## ❓ Jawaban Pertanyaan-Pertanyaanmu

| Pertanyaan | Jawaban Singkat | Detail |
|---|---|---|
| Butuh API untuk harga real-time? | **Ya.** Paling murah & bagus: package Python `MetaTrader5` + akun demo broker = tick real-time XAUUSD **gratis** | [docs/01](docs/01-PANDUAN-API.md) |
| Telegram butuh API juga? | **Ya**, tapi gratis dan gampang: token dari @BotFather + HTTP request biasa | [docs/01](docs/01-PANDUAN-API.md) |
| Risk:Reward paling ideal? | Konsensus trader profesional: **minimal 1:1.5, ideal 1:2 untuk scalping**, risk 0.5–1% per trade | [docs/03](docs/03-RISK-MANAGEMENT.md) |
| Analisa news FOMC dll? | Robot ini pakai **news filter**: berhenti trading ±60 menit sekitar news high-impact (kalender ekonomi otomatis) | [docs/01](docs/01-PANDUAN-API.md) & `bot/news/` |
| 5–10% per hari bisa? | **Tidak secara konsisten.** Target realistis: 5–15%/bulan dengan drawdown terkendali | [docs/03](docs/03-RISK-MANAGEMENT.md) |

## ⚠️ Disclaimer

Trading leverage instrumen seperti XAUUSD berisiko tinggi. Kode ini adalah alat bantu
dan bahan belajar, **bukan jaminan profit**. Selalu mulai dari akun demo. Kerugian
sepenuhnya tanggung jawab pengguna.
