# 04 — Roadmap: Perjalanan Panjang Menyempurnakan Robot

Kamu benar — bikin robot trading itu perjalanan panjang. Ini peta jalannya supaya
kamu tidak tersesat, disusun dari pengalaman kolektif komunitas algo trading
(luar negeri & Indonesia). Jangan loncat fase.

## Fase 0 — Fondasi (kamu di sini) ✅
- [x] Kerangka robot: data feed, strategi MTF, risk manager, news filter, Telegram, backtester
- [ ] Buka akun demo MT5, setup bot Telegram, isi `config.yaml`
- [ ] Jalankan `python main.py --mode signal` — pastikan sinyal masuk ke Telegram

## Fase 1 — Backtest (2–4 minggu kerja)
Tujuan: buktikan strategi punya edge di data masa lalu SEBELUM uang terlibat.

- [ ] Kumpulkan data M5/M15/H1 XAUUSD minimal **2 tahun** (dari MT5:
      `copy_rates_range`, atau download dari broker/histdata)
- [ ] Jalankan `python main.py --mode backtest`
- [ ] Kriteria lulus (kalau tidak lulus, kalibrasi parameter, ulangi):
  - Profit factor > 1.3 (net, SETELAH spread + komisi + slippage realistis)
  - Max drawdown < 15–20%
  - Minimal 200+ trade dalam sampel (sampel kecil = kebetulan)
  - Profit tidak bergantung pada 1–2 trade raksasa
- [ ] **Walk-forward test**: optimasi di 2019–2023, uji buta di 2024–2025.
      Kalau hasil uji buta jelek → strategi overfit → ulangi.

⚠️ **Jebakan #1 pemula: overfitting.** Kalau kamu utak-atik parameter sampai
backtest bagus sempurna, kamu tidak menemukan edge — kamu menghafal masa lalu.
Makin sedikit parameter, makin bagus. Curigai hasil backtest yang "terlalu indah".

⚠️ **Jebakan #2: biaya transaksi.** Scalping = banyak trade = spread & komisi
menggerus. Backtest WAJIB memasukkan spread realistis (0.15–0.35 untuk gold raw
account) + slippage. Strategi yang profit tanpa biaya dan rugi dengan biaya = rugi.

## Fase 2 — Forward Test di Demo (minimal 3 bulan)
- [ ] Jalankan `--mode live` di akun DEMO 24 jam (VPS)
- [ ] Bandingkan hasil vs backtest periode sama — kalau jauh berbeda, cari sebabnya
      (biasanya: spread real, slippage, requote, bug logika waktu/timezone)
- [ ] Review mingguan: baca log CSV, kelompokkan loss (kena news? sesi salah? SL kesempitan?)
- [ ] Perbaiki SATU hal per iterasi, catat setiap perubahan (git commit!)

## Fase 3 — Live Kecil (3–6 bulan)
- [ ] Modal kecil yang kamu SIAP hilangkan 100% (mis. $100–500)
- [ ] Risk tetap 0.5%/trade — tujuannya validasi eksekusi real, bukan cari uang
- [ ] Ukur: slippage real, spread saat entry, perbedaan vs demo
- [ ] 3 bulan profit konsisten + drawdown terkendali → baru naikkan bertahap

## Fase 4 — Scale
- Naikkan modal bertahap ATAU ikut prop firm challenge (FTMO, FundedNext, dll)
  — dengan robot yang terbukti, akun funded $50–200k jauh lebih masuk akal
  daripada memaksa % gila di modal kecil
- Diversifikasi: tambah strategi kedua yang tidak berkorelasi (misal mean-reversion
  sesi Asia) — portofolio strategi lebih stabil dari satu strategi

## Fase 5 — Peningkatan Lanjutan (setelah dasar terbukti)
- News trading (baca actual vs forecast dari kalender, entry searah surprise)
- Analisa sentimen headline dengan LLM/AI
- Filter volatilitas adaptif (regime detection)
- Dashboard web monitoring
- Machine learning untuk filter sinyal (hati-hati: 95% penerapan ML retail = overfit)

## Prinsip Sepanjang Jalan
1. **Satu perubahan per waktu**, selalu lewat backtest dulu.
2. **Journal semuanya** — robot ini sudah auto-log ke CSV.
3. **Uptime & bug adalah risiko nyata**: robot mati saat posisi terbuka = bahaya.
   Pakai VPS + Telegram alert koneksi putus.
4. **Jangan beli EA "winrate 95%"** — hampir pasti martingale/grid yang akan MC.
5. **Komunitas**: belajar dari forum berkualitas (Forex Factory, r/algotrading,
   komunitas algo Indonesia di Telegram/Discord), tapi verifikasi semua klaim
   dengan backtest-mu sendiri. Jangan percaya screenshot profit siapa pun.
