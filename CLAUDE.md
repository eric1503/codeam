# Konteks Proyek — Konten Kopi Dustin

Dokumen ini dibaca otomatis oleh sesi Claude Code berikutnya di repo ini.
Tujuannya supaya konteks tidak hilang antar sesi. **Kalau ada keputusan baru,
tambahkan ke sini.**

---

## 1. Tentang Orang & Proyek

- **Nama:** Dustin (Eric Angelo / `eric1503`, `ericangelo1503@gmail.com`)
- **Instagram:** `@Dustin_wijaya04` — ini yang dipakai sebagai label di semua carousel
- **Tempat kerja / brand:** **Terroir IDN** (by Terroir Lab), Hampton Avenue Blok H No 5, Gading Serpong
- **Topik konten:** kopi — seduh manual, sains kopi, edukasi pemula
- **Panggilan ke asisten:** "Josh"

### Dua halaman kerja yang dia pakai
- **Halaman ini (repo `eric1503/codeam`)** — KHUSUS SCRIPT & materi konten
- **"Dustin V2"** — halaman terpisah, isinya semua artifact. **Sengaja dipisah biar tidak tercampur.**
  Catatan: percakapan di halaman V2 TIDAK terbawa ke sini. Kalau butuh konteks dari sana,
  Dustin harus menyalinkannya.

---

## 2. Sistem Konten (dari catatan tulis tangan Dustin)

### Struktur HEIA — dipakai di semua script
| Bagian | Fungsi |
|---|---|
| **Hook** | Bikin orang berhenti scroll — **selesai sebelum detik ke-8** |
| **Empathy** | Bikin orang merasa "ini gue banget" |
| **Isi** | Kasih value |
| **Aksi** | Ajak lakukan sesuatu |

### Jadwal posting — tayang jam 18.00
| Hari | Funnel |
|---|---|
| Senin | TOFU |
| Selasa | MOFU |
| Rabu | TOFU |
| Kamis | MOFU |
| Jumat | BOFU |
| Sabtu | MOFU |
| Minggu | TOFU |

Target: **TOFU 3× · MOFU 3× · BOFU 1×** per minggu.
Volume: **2 carousel/minggu · 1–2 YouTube long form · 7–10 short/minggu.**
Tiap Minggu: analisa performa terhadap dashboard.

### Resep V60 miliknya
Dose 15 g · suhu 92 °C · rasio 1:15 · open switch di 0:50 · close switch 1:30 · selesai ±1:45 (150–200 ml).

### Rencana MOFU
1. Endorse mesin **Ecobrew**
2. Pentingnya menakar saat menyeduh

---

## 3. Preferensi Dustin — WAJIB DIPATUHI

1. **Semua script dalam format Word (.docx)**, bukan markdown — supaya bisa diedit langsung.
   Kalau dia sudah mengedit sendiri, JANGAN generate ulang dari nol; edit file itu langsung.
2. **Bahasa harus ramah pemula.** Nol istilah teknis tanpa penjelasan. Nol nama senyawa kimia
   diucapkan di narasi (boleh muncul sebagai teks kecil di layar).
3. **Jangan pakai kalimat yang menyinggung** atau bikin penonton merasa bodoh/disalahkan.
   Patokan: *"apakah orang yang cuma minum kopi sachet merasa dilibatkan, atau merasa disindir?"*
4. **Analogi jangan dipakai di semua konten** — membosankan. Maksimal **satu analogi per konten**,
   dan hanya kalau penonton butuh dijelaskan *kenapa*-nya. Konten yang isinya daftar/angka
   lebih baik tanpa analogi sama sekali.
5. **Tiap klaim harus ada sumbernya**, disebut di narasi DAN muncul di layar. Sertakan buku
   dan jurnal kalau ada. Selalu bikin tabel klaim → sumber.
6. **Level bukti** dipakai di semua materi: `BUKTI KUAT` (peer-review langsung) ·
   `BUKTI SEDANG` (konsensus praktisi / riset bidang lain) · `KLAIM PRODUSEN`.
7. **JANGAN kasih "PR"/tugas di setiap carousel.** Slide ajakan aksi sudah dihapus dari
   carousel air atas permintaannya. Konten boleh berakhir di ringkasan atau sumber.
8. **Format poin lebih disukai** daripada paragraf panjang — gaya catatan tulis tangannya:
   satu baris, satu fungsi.

---

## 4. Standar Desain Carousel

- Ukuran **1080×1350** (4:5), dirender **2×** → 2160×2700
- Latar gelap `#0B0B0D`, headline **putih murni** `#FFFFFF`, body 88% putih, aksen amber `#FFC978`
- **Teks sengaja dibuat terang** karena Dustin menimpanya dengan foto background sendiri lalu
  menggelapkan foto itu
- Selalu render **dua versi**: `jpg/` (siap pakai) dan `png-transparan/` (buat ditimpa foto)
- **Label pojok kiri bawah: `@Dustin_wijaya04`** — casing persis begitu, jangan di-uppercase
- Pojok kanan bawah: nomor slide `01 / 10`. Slide pertama pakai `geser →`
- Font: Liberation Sans (fallback DejaVu Sans) — Google Fonts tidak bisa dimuat di environment ini

### Cara render ulang
Generator ada di scratchpad (hilang tiap sesi baru). Kalau perlu dibuat ulang:
Node + `playwright-core`, Chromium di `/opt/pw-browsers/chromium-1194/chrome-linux/chrome`.
Render HTML → screenshot JPEG quality 94 / PNG `omitBackground: true`.

---

## 5. Yang Sudah Dibuat

### `scripts/` — dokumen Word
| File | Isi |
|---|---|
| `TOFU 01 - Tasting Note Kopi.docx` | Apakah kopi bisa keluarkan rasa sesuai tasting note. Analogi: "resep chef" (satu-satunya, hanya di bagian twist) |
| `TOFU 02 - Nyeduh per Roast Level.docx` | Light = kentang · Medium = ayam · Dark = bayam. **Ini satu-satunya konten yang analoginya penuh** |
| `TOFU 03 - Kopi 98 Persen Air.docx` | Kandungan air per ion. **Tanpa analogi**, format daftar |
| `EVENT - Bar Takeover Andika Nugraha.docx` | Rencana konten acara 20 Agt 2026 |

### `carousel/` — gambar siap posting
| Folder | Isi |
|---|---|
| `air-98-persen/` | 10 slide (slide PR sudah dihapus) |
| `rpm-grindsize/` | 12 slide |

---

## 6. Temuan Riset yang Sudah Diverifikasi

**Jangan riset ulang dari nol — pakai ini.**

### Tasting note
- Kopi sangrai: **1.000+ senyawa aroma**, hanya ±5% relevan (MDPI Foods 2023)
- Senyawa buah di kopi = senyawa yang sama di buah aslinya (PMC9407621, MDPI Molecules 2023)
- **WCR Sensory Lexicon**: 110 atribut, tiap kata punya benda referensi
- **Q Grader** (CQI): 20 ujian, 9 modul, **rekalibrasi tiap 3 tahun**
- Insight kunci: Q Grader dilatih supaya lidahnya **SERAGAM**, bukan supaya istimewa
- Efek ekspektasi nyata: Siegrist & Cousin, *Appetite* (2009)

### Roast level
- Makin lama disangrai → makin berpori → makin mudah ditembus air
- Patokan SCA: **90–96 °C**. Light 94–96 · Medium 92–94 · Dark 90–92
- ⚠️ Angka per roast level itu **patokan industri, bukan standar resmi SCA**. Di video sebut
  "patokan umum", jangan "standarnya"

### Air
- Kopi filter = **±98% air** (espresso ±90% — jangan digeneralisir!)
- Hendon dkk. (2014), *J. Agric. Food Chem.*, DOI 10.1021/jf501687c — magnesium mengikat asam
  sitrat/malat/laktat lebih kuat dari kalsium
- **Heliyon (2024)**, PMC10907646 — ion lebih mengubah **persepsi** rasa daripada jumlah yang
  terekstrak. Ini yang jadi twist: *"air itu tombol volume"*
- Natrium menekan reseptor pahit → manis lebih terbaca (*J. Agric. Food Chem.* 2024,
  DOI 10.1021/acs.jafc.3c08775)
- Sulfat/klorida/kalium = **BUKTI SEDANG** (dasarnya kimia air bir; Barista Hustle justru
  bilang efeknya kecil di kadar kopi)
- **Koreksi dari catatan asli Dustin:** magnesium (bukan kalsium) yang mengikat asam sitrat
- Apax Lab TONIK/JAMM/LYLAC — komposisi terverifikasi, tapi klaim rasanya = **klaim produsen**

### RPM & grind size
- Fines = partikel <100 mikron; jumlahnya lebih menentukan waktu ekstraksi daripada rata-rata
  ukuran partikel (*Scientific Reports* 2024)
- Klaim "RPM rendah = fines lebih sedikit" = **BUKTI SEDANG**. Coffee ad Astra menganalisa
  **300 PSD dari 24 grinder**: efeknya sangat tergantung grinder & burr
- Panas: ruang giling bisa 80–100 °C. **Kontra-intuitif** — grinder hangat justru menghasilkan
  fines lebih SEDIKIT (Barista Hustle)
- **RDT / semprot air** = paling terbukti (*Matter* 2023, triboelektrifikasi). Light roast
  cenderung bermuatan positif, dark negatif
- *Matter* (2020) "Systematically Improving Espresso" — ada **batas kehalusan**; lewat dari itu
  ekstraksi justru turun. Rekomendasi: kopi lebih sedikit, giling lebih kasar

### Crema
- Terbentuk dari CO₂ terlarut di 9 bar yang keluar dari larutan saat tekanan drop
- Distabilkan surfaktan: melanoidin (warna), protein, polisakarida/galaktomanan, lipid
- **Illy & Viani (2005)**: konvensi crema ≥10% volume, bertahan ≥2 menit
- **Crema BUKAN penanda kualitas** — kopi basi & robusta tetap menghasilkan crema
- Crema cenderung **pahit & astringen**; bagian bawah lebih manis (BUKTI SEDANG)
- Buku: **Jonathan Gagné — *The Physics of Espresso***, terpisah dari *The Physics of Filter Coffee*

---

## 7. Buku Rujukan

| Buku | Dipakai untuk |
|---|---|
| *Water for Coffee* — Colonna-Dashwood & Hendon (2015) | Air |
| *Water: A Comprehensive Guide for Brewers* — Palmer & Kaminski | Sulfat vs klorida (buku bir) |
| *SCA Water Quality Handbook* | Angka patokan air |
| *The Physics of Espresso* — Jonathan Gagné | Espresso, crema |
| *The Physics of Filter Coffee* — Jonathan Gagné (2020) | Seduh filter |
| *Espresso Coffee: The Science of Quality* — Illy & Viani (2nd ed.) | Espresso, crema |
| *The Professional Barista's Handbook* — Scott Rao (2008) | Grinding (bacaan lanjutan) |
| *The Craft and Science of Coffee* — ed. Britta Folmer | Bacaan lanjutan — **bukan sumber angka** |

---

## 8. Catatan Kerja

- **Git:** kembangkan di branch `claude/coffee-tasting-notes-mhe48b`. PR #1 masih draft & open.
- **Automation:** langganan PR activity & check-in terjadwal **sudah dimatikan** atas permintaan
  Dustin. Jangan dihidupkan lagi tanpa diminta.
- **Environment:** WebFetch diblokir egress — hanya WebSearch yang jalan. LibreOffice tidak bisa
  memuat docx, jadi verifikasi dokumen lewat isi XML, bukan render PDF.
- **Kebiasaan Dustin:** dia menghargai koreksi faktual. Sudah dua kali terselamatkan dari salah
  fatal — gelar "World" vs "Indonesia" Barista Champion, dan kalsium vs magnesium.
  **Selalu cek klaimnya sebelum dibuatkan konten.**
