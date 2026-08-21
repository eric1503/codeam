# 03 — Risk Management, RR Ideal, dan Ekspektasi yang Jujur

Ini dokumen paling penting di repo ini. Strategi menentukan 20% hasil;
risk management + psikologi menentukan 80% (konsensus hampir semua trader
profesional, dari Mark Douglas sampai Van Tharp).

---

## A. Kenapa 5–10% per Hari Tidak Mungkin Konsisten

Mari pakai matematika, bukan opini:

**1) Compounding-nya mustahil.**
Modal $1.000 dengan 5%/hari, 22 hari trading/bulan:
- 1 bulan: $2.925
- 6 bulan: $626 ribu
- 12 bulan: $392 JUTA
- 18 bulan: melebihi kekayaan orang terkaya dunia.

Kalau ini mungkin, semua bank dan hedge fund sudah melakukannya. Kenyataan:

| Siapa | Return |
|---|---|
| Renaissance Medallion (hedge fund terbaik sepanjang sejarah) | ±66%/TAHUN |
| Warren Buffett (rata-rata karir) | ±20%/TAHUN |
| Trader prop firm yang lolos & dibayar (minoritas kecil) | 5–15%/BULAN, tidak stabil |
| Target FTMO Challenge | 10% TOTAL (tanpa batas waktu), dengan max daily loss 5% |

Perhatikan: **prop firm menjadikan -5% SEHARI sebagai syarat gagal**. Industri
sudah memberi tahu kita bahwa ±5% sehari itu wilayah bahaya, bukan target.

**2) Risk of ruin.**
Untuk berpeluang dapat 5–10%/hari dari scalping, kamu harus risk besar per trade
(5–15%+). Dengan win rate 50% dan risk 10%/trade, probabilitas kena 5 loss beruntun
dalam 100 trade itu hampir pasti terjadi → akun -40% sekali seri → secara psikologis
kamu akan revenge trade → habis. Ini bukan "kalau", tapi "kapan".

**3) Target harian itu sendiri merusak.**
Market tidak memberi peluang yang sama tiap hari. Memaksa target harian = memaksa
entry di hari yang tidak ada setup = overtrading. Robot ini justru dibatasi
maksimal N trade/hari dan berhenti kalau daily loss tercapai.

**Target yang benar untuk robot scalping yang baik:**
- Bulan pertama-pertama: **tidak MC / drawdown terkendali** (itu saja sudah prestasi)
- Realistis jangka panjang: **3–10%/BULAN** dengan max drawdown < 15%
- Kalau konsisten 6–12 bulan → scale up modal, atau daftar prop firm
  (dengan modal $100k funded, 5%/bulan = $5.000/bulan ≈ Rp 80 juta/bulan —
  ini jalur yang DIPAKAI trader-trader muda kompeten sekarang, bukan 10%/hari).

---

## B. Risk:Reward Ratio Paling Ideal (Riset dari Sumber Kompeten)

Tidak ada satu angka ajaib — RR ideal tergantung win rate strategi. Rumus dasarnya
(dari Van Tharp, *Trade Your Way to Financial Freedom*):

```
Expectancy = (WinRate × AvgWin) − (LossRate × AvgLoss)
```

Harus positif setelah dikurangi spread + komisi + slippage.

| RR | Win rate minimal agar break-even | Cocok untuk |
|---|---|---|
| 1:1 | > 50% | Scalping sangat cepat (butuh win rate tinggi, berat lawan spread) |
| **1:1.5** | > 40% | **Batas bawah yang disarankan untuk scalping gold** |
| **1:2** | > 33.3% | **Sweet spot — default robot ini** |
| 1:3 | > 25% | Intraday/swing, sinyal lebih jarang kena TP |

Konsensus dari sumber-sumber yang paling dihormati:

- **Van Tharp** (psikolog trading, riset ribuan trader): fokus pada expectancy dan
  position sizing, bukan win rate. Risk per trade kecil (≤1%) supaya bisa bertahan
  melewati losing streak yang PASTI datang.
- **Mark Douglas** (*Trading in the Zone*): edge apapun butuh sampel besar; satu
  trade tidak berarti apa-apa. Risk kecil = bisa main ratusan sampel.
- **Alexander Elder**: aturan 2% per trade dan "6% rule" — berhenti trading sebulan
  itu kalau total loss bulan berjalan kena 6%.
- **Al Brooks / Bob Volman** (scalper price action): scalping realistis di RR 1:1
  sampai 1:2 dengan win rate 50–60%, dan biaya transaksi adalah musuh terbesar scalper.
- **Larry Hite** (Market Wizards): "Kalau kamu tidak bertaruh, kamu tidak bisa menang.
  Kalau kamu kehilangan semua chip, kamu tidak bisa bertaruh."
- **Praktik prop firm (FTMO dkk)** — de facto standar industri sekarang, dipakai juga
  oleh komunitas trader funded Indonesia: risk 0.5–1% per trade, max daily loss
  pribadi 2–3% (di bawah batas resmi 5%), RR minimal 1:2.
- **Kelly Criterion** (matematika sizing optimal): hampir semua praktisi memakai
  "fractional Kelly" (¼–½ Kelly) karena full Kelly terlalu volatile — hasilnya
  biasanya jatuh di kisaran 0.5–2% risk per trade. Selaras dengan semua di atas.

**Default robot ini (bisa diubah di `config.yaml`):**
- Risk per trade: **0.5%** (konservatif; naikkan ke 1% setelah 3 bulan forward test bagus)
- RR: **1:2**, breakeven di 1R
- Max daily loss: **2%** → robot berhenti sampai besok
- Max trades/hari: **5**
- Max posisi bersamaan: **1**

---

## C. Position Sizing XAUUSD (Cara Robot Menghitung Lot)

Spesifikasi umum XAUUSD (cek broker masing-masing):
- 1 lot standard = 100 oz
- Pergerakan $1.00 pada harga gold = $100 per 1.0 lot
- "1 pip gold" umumnya = $0.10 pergerakan harga = $10/lot

**Rumus robot (`bot/risk/risk_manager.py`):**

```
risk_uang   = balance × risk_per_trade          (mis. $1.000 × 0.5% = $5)
jarak_sl    = |entry − SL| dalam dolar harga     (mis. $3.50)
nilai_per_$ = contract_size = 100                 (per 1.0 lot)
lot         = risk_uang / (jarak_sl × 100)        (mis. 5 / 350 = 0.014 → 0.01 lot)
```

Lot dibulatkan KE BAWAH ke step broker (0.01). Kalau hasil < lot minimum broker,
robot **skip trade** (bukan memaksa risk lebih besar).

---

## D. Aturan Bertahan Hidup (Hard Rules yang Ditegakkan Robot)

1. Tidak ada trade tanpa SL. Tidak pernah.
2. SL tidak pernah digeser menjauh. Robot tidak punya fitur itu, sengaja.
3. Daily loss limit kena → berhenti total sampai hari berikutnya.
4. Tidak menambah posisi loss (no averaging down / martingale).
   **Martingale = penyebab #1 robot "profit 6 bulan lalu MC dalam 1 hari".**
   Banyak EA komersial yang dijual dengan "winrate 95%" adalah martingale/grid —
   kurva profitnya mulus sampai tiba-tiba akun habis. Hindari.
5. News high-impact → tidak entry, dan (opsional) tutup posisi sebelum event.
6. Setiap trade tercatat (CSV + Telegram) untuk evaluasi mingguan.
