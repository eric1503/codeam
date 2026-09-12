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
8a. **MULAI DARI MASALAH, BUKAN DARI ISTILAH.** Ini kritik langsung Dustin di carousel grinding versi
   pertama: terlalu advanced, kurang "ngena". Pola yang dia mau — tiap slide dibuka dengan **keluhan
   yang orang beneran rasain**, ditulis seperti kalimat mereka sendiri (pakai tanda kutip), BARU
   dijelaskan penyebabnya. Jangan buka slide dengan nama konsep (bimodal, difusi, triboelektrifikasi).
   Istilah teknis boleh ada, tapi taruh di daftar sumber, bukan di headline.
8b. **JANGAN tulis koreksi di dalam materi jadi.** Kalau ada yang salah di draf Dustin, langsung tulis
   versi benarnya tanpa menyebut versi lama. Sampaikan koreksinya lewat chat saja. Alasannya: kalau
   koreksi muncul di dokumen, orang mengira Dustin yang kasih informasi salah.
8c. **Cantumkan link sumber penuh dan klikabel di akhir tiap kalimat** — bukan cuma nomor `[n]`.
   Tiap gambar juga dikasih link sumbernya.
9. **Jangan bikin klaim yang bisa menyinggung kelompok manapun.** Dustin sudah minta satu slide
   dihapus karena membandingkan robusta dengan arabika — Indonesia produsen robusta besar, dan
   itu bisa menyinggung petani serta pelaku industri. Sebelum menulis perbandingan, tanya:
   *"apakah ada kelompok yang bisa merasa direndahkan?"* Kalau iya, cari sudut lain.

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
- **Subtitle Inggris** (sejak permintaan Dustin): tiap eyebrow, headline, body, dan item punya
  versi Inggris di bawahnya — *italic*, lebih redup (45–52% putih), ukuran lebih kecil. Body
  Inggris dikasih garis aksen di kiri. Tujuannya penonton luar negeri ikut ngerti tanpa teks
  Inggrisnya rebutan perhatian sama teks Indonesia.
- Slide dengan **4 item atau lebih** otomatis pakai mode `dense` (font dikecilin) biar ga kepotong.
  Bisa juga dipaksa manual lewat flag `dense: true` di slide-nya
- **Subtitle Inggris bisa dimatikan** — cukup jangan pass env `EN` ke `render.js`. Dustin minta ini
  di carousel `grinding/`. Tanpa EN, ruang slide jadi jauh lebih lega (nol overflow)
- **Palet hitam putih** tersedia lewat env `MONO=1` — aksen amber diganti putih, `h1` jadi 80% putih
  dengan `<em>` putih penuh sebagai penekanan. Dipakai di carousel paper-filter atas permintaan Dustin

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
| `MOFU - PPM Air untuk Filter Coffee.docx` | Sweet spot 100–150 ppm buat filter coffee (SCA ideal 150, rentang 75–250) |
| `MOFU - Termal vs Mekanik.docx` | Kerangka dua energi dari sketsa Dustin — suhu (termal) vs flow/agitasi (mekanik), struktur (grind size) sbg kanvas |
| `SCRIPT - Nicaragua La Bastilla Geisha Washed.docx` | **Link sumber penuh & klikabel di akhir tiap kalimat** + 6 grafis tertanam (grafisnya di `assets/gfx-labastilla/`). Bagian resep sengaja dikosongkan — Dustin isi sendiri |

### `carousel/` — gambar siap posting
| Folder | Isi |
|---|---|
| `air-98-persen/` | 10 slide (slide PR sudah dihapus) |
| `rpm-grindsize/` | 11 slide |
| `crema-espresso/` | 11 slide |
| `kafe-vs-rumah/` | 9 slide |
| `paper-filter/` | 9 slide — **PALET HITAM PUTIH**, bukan amber |
| `dripper-material/` | 12 slide — bahan dripper & **arah rasa** (peta rasa dari Dustin) |
| `termal-mekanik/` | 11 slide — dua energi & satu kanvas |
| `aroma-floral/` | 7 slide — cara nonjolin aroma floral |
| `rasio-1-15/` | 8 slide — kenapa 1:15 dianggap golden ratio |
| `cut-brew/` | 7 slide — teknik motong seduhan sebelum selesai |
| `grinding/` | 9 slide — **TANPA subtitle Inggris**, struktur **masalah-dulu** |
| `perkolasi/` | 9 slide — perjalanan air lewat bubuk, struktur **masalah-dulu** |

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
- **Bora dkk. (2026)**, *Journal of Food Process Engineering* — "Characterization of Bimodal Particle
  Size Distribution of Ground Coffee Powder". Hampir semua sampel kopi menghasilkan sebaran **bimodal**
  (dua puncak: fines + boulders). Di setelan paling halus, pecahnya fraksi kasar bikin sebaran bimodal
  yang lemah dengan puncak fines yang menonjol
- **Gagné, 300 PSD dari 24 grinder** (Coffee ad Astra, 2023): **burr flat menghasilkan ukuran partikel
  lebih seragam** dibanding conical. PSD 10–1200+ mikron cocok dimodelkan dengan log-normal tiga komponen.
  ⚠️ Nuansa penting: **cara burr memotong vs menggerus lebih menentukan bentuk sebaran** daripada sekadar
  label flat/conical. Gagné juga bikin aplikasi pengukur PSD dari foto/scan
- Conical = bimodal → body lebih tebal, clarity turun. Flat = unimodal → clarity naik, fines lebih sedikit
  (level BUKTI SEDANG — sangat tergantung grinder & burr)

### Crema
- Terbentuk dari CO₂ terlarut di 9 bar yang keluar dari larutan saat tekanan drop
- Distabilkan surfaktan: melanoidin (warna), protein, polisakarida/galaktomanan, lipid
- **Illy & Viani (2005)**: konvensi crema ≥10% volume, bertahan ≥2 menit
- **Crema BUKAN penanda kualitas** — kopi basi & robusta tetap menghasilkan crema
- Crema cenderung **pahit & astringen**; bagian bawah lebih manis (BUKTI SEDANG)
- ⚠️ Slide soal robusta vs arabika **sudah dihapus** atas permintaan Dustin — berisiko menyinggung
- Buku: **Jonathan Gagné — *The Physics of Espresso***, terpisah dari *The Physics of Filter Coffee*

---

### PPM air untuk filter coffee
- SCA Golden Cup: ideal **150 ppm TDS**, rentang aman **75–250 ppm**
- Filter coffee (beda dari espresso) sweet spot praktisi: **100–150 ppm** — ini **konsensus praktisi**,
  bukan angka resmi terpisah dari SCA. Jangan bilang "SCA bilang khusus filter coffee segini"
- TDS sama ≠ rasa sama — komposisi mineral (Mg/Na/bikarbonat) tetap nentuin, lihat riset air di atas
- Buku *Physics of Filter Coffee* Gagné: ada bab air, tapi ga ketemu angka ppm spesifik lewat
  pencarian — dipakai sebagai rujukan konsep (alkalinitas vs kesadahan), bukan sumber angka

### Termal vs Mekanik (dari sketsa tangan Dustin, disempurnakan dengan riset dia sendiri)
- **Koreksi penting:** versi awal makai "Kinetik" — diganti ke **"Mekanik"** karena "kinetics" di
  literatur ekstraksi kopi udah punya arti sendiri (laju ekstraksi thd waktu, gabungan suhu+partikel+flow),
  bukan "energi gerak". Pakai "kinetik" di sini tabrakan makna sama paper yang jadi sumbernya sendiri.
  ⚠️ **Ini catatan internal, JANGAN dijadikan slide.** Slide yang ngebahas "kenapa mekanik bukan kinetik"
  sudah dihapus atas permintaan Dustin — bisa jadi bumerang, karena kelihatan kayak ngoreksi istilah
  orang lain di depan umum. Cukup pakai "Mekanik" tanpa menjelaskan kenapa
- **Bahasa:** sebut **"variabel"**, jangan "tombol". Dustin ga suka metafora tombol/knob — kurang enak
  didengar. Berlaku di semua materi, bukan cuma carousel ini
- Kerangka final: **Termal** (suhu) + **Mekanik** (flow/tuangan/agitasi) = dua energi. **Struktur**
  (ukuran gilingan, fines) BUKAN energi ketiga — itu "kanvas" yang nentuin jarak difusi (model Moroney dkk.)
- 6 sumber (semua terverifikasi, dari riset Dustin sendiri — kualitasnya lebih tinggi dari kerangka awal):
  Wang & Lim (2021, suhu 4-93°C, makin panas makin cepat ekstraksi) · Sano dkk. (2019, model mass-transfer,
  flow+partikel+stirring) · Ahmed dkk. (2019, agitasi naikin TDS signifikan) · model double-porosity
  Moroney dkk. (broken cells vs intact cells, Hukum Darcy) · Schmieder dkk. (2023, Foods 12(15):2871 —
  flow rate variabel PALING dominan) · Gagné/Coffee ad Astra (agitasi berlebih → fines migrasi → clogging)
- Framing di video: "kalau disederhanain, ada dua energi dan satu kanvas" — bukan "riset bilang cuma
  ada dua kategori resmi". Ini sintesis dari 6 studi, bukan istilah baku satu paper

### Paper filter (kertas filter)
- **Cafestol/kahweol**: paper filter 12 mg/L · mesin kantor 176 mg/L · kopi rebus **939 mg/L**
  (Uppsala University, 2025). Temuan menarik: sebagian besar cafestol tertahan di AMPAS, bukan kertasnya
- **Gagné** periksa **13 kertas filter di bawah mikroskop** — anyaman serat beda = laju alir beda
- **James Hoffmann** metode uji rasa kertas: rendam di air panas, cicipi airnya. Unbleached lebih
  kuat rasa kertasnya; kertas merek sama dari pabrik beda pun rasanya beda
- **Sibarist FAST**: serat abaca + selulosa, oxygen-bleached, klaim 15–40% lebih cepat, ~8× harga Hario
- **Hiflux**: buatan Korea, serat **lyocell** + anyaman 3D, klaim sampai **42%** lebih cepat.
  Bedanya: Hiflux sengaja **ngelolosin lebih banyak minyak + sedikit fines** → body lebih tebal
- ⚠️ Angka 15–40% dan 42% itu **KLAIM PRODUSEN** — belum ada uji independen terkontrol yang
  membandingkan keduanya
- **Abaca** = spesies **pisang** (*Musa textilis*), bukan hemp. Serat dari pelepah daun, panjang 1–3 m,
  serat alami terkuat, kandungan selulosa 56–68%. **Selulosa** di daftar bahan = bubur kayu (serat pendek).
  Jadi bukan dua bahan beda — dua PANJANG SERAT beda

### Bahan dripper (keramik · kaca · stainless · plastik)
- Konduktivitas termal: **plastik AS/PP ±0,33 · kaca ±0,9 · keramik ±4 · stainless 304 ±16 W/(m·K)**.
  Ini data sifat bahan standar, **bukan** hasil riset kopi
- Dua sifat yang main: **konduktivitas** (cepat-lambatnya panas lewat) + **massa termal**
  (banyak-sedikitnya panas yang harus diserap sebelum bendanya sendiri hangat — dinding tebal = besar)
- Dripper **ga dipanasin duluan**: air ±95 °C bisa turun ke **±82 °C** (≈20 derajat). Patokan SCA 90–96 °C
- ⚠️ **Tapi kalau semuanya di-preheat, selisihnya cuma 1–2 °C** (Andytown, uji berdampingan: 2–4 °F;
  plastik tertinggi, keramik terendah). Jadi angka 20 derajat itu soal preheat, bukan soal bahan
- Uji rasanya **saling bertentangan**: ada yang bilang plastik nendang/kaca bersih/keramik bulat,
  ada yang bilang plastik & kaca sama persis. Stainless malah berperilaku mirip plastik (dinding tipis)
- ⚠️ **BELUM ADA riset peer-review khusus soal bahan dripper.** Semua uji yang ada = uji praktisi.
  Jangan sebut angka bahan→rasa sebagai fakta
- Plastik dipakai Hoffmann, Scott Rao, dan sebagian besar juara World Brewers Cup — alasannya
  **konsistensi**, bukan "rasanya lebih enak"
- Rantai bukti yang sah: bahan→suhu = BUKTI SEDANG (uji praktisi); suhu→ekstraksi = BUKTI KUAT (Wang & Lim)
- Sumber praktisi: Andytown Coffee Roasters · Home-Barista forum · Basic Barista "Metal vs Ceramic V60" ·
  Barista Hustle P 1.01 Preheating · Gagné (massa termal & insulasi brewer)
- **Peta arah rasa versi Dustin** (dipakai di carousel, level BUKTI SEDANG): plastik → manis, clarity,
  aromatik · kaca → acidity paling kebaca · keramik → kompleks & bulat · stainless → aftertaste bersih
  & ekstraksi tinggi. Sudah dicek: peta ini **konsisten sama fisikanya** (makin sedikit panas yang
  diambil dripper → suhu makin stabil → ekstraksi makin rata). Tapi tetap uji praktisi, bukan riset
- **Framing yang dipakai:** "dripper nentuin ARAH rasa", bukan "dripper bikin enak/ga enak", dan bukan
  "dripper nyuri panas" (hook itu ditolak Dustin — terlalu negatif)
- Syarat mutlak yang selalu disebut bareng peta rasa: **kalau ga di-preheat, arah rasanya ga muncul
  sama sekali**. Stainless paling bergantung preheat karena massanya paling kecil

### Aroma floral
- Senyawa floral = **terpen** (linalool, geraniol). **Bawaan varietas/ketinggian/proses** — seduhan bisa
  nonjolin atau ngilangin, **tapi ga bisa bikin dari nol**. Ini framing wajib, biar ga overclaim
- Gesha punya linalool & limonene tinggi; landrace Etiopia juga tinggi ekspresi terpennya
- **Foods 10(6):1347 (2021)**, PMC8230519 — kondisi sangrai & metode ekstraksi = faktor signifikan buat
  senyawa aroma. **Gilingan lebih halus → sinyal senyawa aroma terukur lebih banyak**
- **SCA staling literature review** — menggiling menaikkan luas permukaan → aroma hilang paling cepat
  tepat setelah digiling. ⚠️ Angka "60% dalam 15 menit" cuma ketemu di blog, **jangan dipakai sebagai
  angka pasti** — cukup bilang "menit-menit pertama"
- **Ketegangan penting:** suhu tinggi menaikkan ekstraksi (Wang & Lim, BUKTI KUAT), TAPI senyawa floral
  itu paling volatil — air panas terus juga nerbangin sebagian ke udara. Jawabannya bukan "panas terus"
- **George Jinyang Peng** — Juara **World Brewers Cup 2025 di Jakarta** (dari Cina), pakai **Solo Dripper**.
  Resep: 15 g · 800 mikron (26–27 klik Comandante C40) · 210 ml · air 40 ppm · **96 °C dua tuangan
  pertama, 80 °C tuangan terakhir** · total 1:45. Framing dia: "temperature is a story from origin to cup"
- Menurut Peng: **aroma paling kebaca ±65 °C, rasa ±50 °C** di cangkir
- ⚠️ **KOREKSI: Solo Dripper BUKAN flat bottom.** Dia hibrida — sudut internal **40°**, dasar melengkung,
  **satu lubang besar**. Rancangan **Jackie Tran** (Mazelab), Juara Brewers Cup Ceko 2024. Flat bottom
  murni itu Kalita Wave / Orea / April. Dustin sempat menyebut "flat bottom seperti Solo" — sudah diluruskan.
  ⚠️ Slide yang membahas ini **sudah dihapus** atas permintaan Dustin. Koreksinya tetap berlaku sebagai
  catatan internal — jangan sebut Solo sebagai flat bottom — tapi jangan dibikin slide lagi

### Kafe vs rumah
- **Resep itu catatan hasil kalibrasi, bukan penyebab rasa** — ini thesis kontennya
- Jendela rasa terbaik kopi: **±7–21 hari setelah sangrai** (light lebih lama, dark lebih cepat)
- Grinder: tiap alat beda sebaran partikelnya (Coffee ad Astra, 300 PSD dari 24 grinder)
- **Charles Spence** (Oxford, 30+ tahun riset persepsi rasa), buku *Gastrophysics* — suasana,
  musik, cahaya, cangkir, dan ekspektasi ikut mengubah rasa yang dipersepsikan
- Kestabilan suhu & tekanan mesin komersial = **BUKTI SEDANG**, jangan sebut angka pasti

---

### Kopi Terroir: Nicaragua La Bastilla Geisha Washed
- Kebun **La Bastilla Coffee Estates**, Jinotega, ±20 km dari kota Jinotega, diapit cagar alam
  **Cerro Datanlí–El Diablo**, dekat **Danau Apanás**. ±300 ha, cuma ±155 ha ditanami kopi.
  Rainforest Alliance sejak 2003. Panen **Des–Mar**. Punya lab QC, mill & fasilitas ekspor sendiri
- Cerita kuat: sekolah dasar 2003 (sekolah terdekat 6 km, mulai 2 guru → 200+ murid), naik jadi
  **sekolah pertanian berasrama 2008**. Ada ecolodge & bio-digester
- **Jinotega = ±80% produksi kopi nasional.** Karakter wilayah: cerah, floral, buah kuning —
  **cocok persis** sama tasting note kemasan (yellow fruits, white florals)
- Kartu skor kemasan: aroma 7 · sweetness 7 · flavour 6 · acidity 6 · **body 3** (disengaja, jangan
  dianggap kelemahan). 1.300–1.500 mdpl = **sedang** buat Geisha, makanya profilnya tea-like bukan meledak
- ⚠️ Skor **84** yang beredar itu buat lot La Bastilla washed LAIN, **bukan** lot Geisha ini. Jangan dipakai

### ⚠️ ATURAN PENTING — CARA MENYAMPAIKAN KOREKSI
Dustin **tidak mau koreksi ditulis di dalam materi jadi** (script/carousel/dokumen). Kalau ditulis di sana,
pembacanya mengira dia pernah kasih informasi salah. **Langsung tulis versi yang benar saja**, tanpa
menyebut versi lamanya. Koreksi cukup disampaikan ke Dustin lewat chat, atau disimpan di CLAUDE.md ini.

### Tiga koreksi di draf PDF Dustin (SUDAH diterapkan diam-diam di docx — jangan tulis sebagai koreksi)
1. **Arah giling per proses kebalik.** Draf: natural halus, washed kasar. Patokan praktisi kebalikannya —
   natural lebih KASAR (gampang larut), washed lebih HALUS (light roast & padat). Draf lamanya juga
   bentrok sama poin ketinggiannya sendiri
2. **Bloom kebalik.** Draf: kopi asam → bloom dikurangi biar manis. Ngurangin bloom = nurunin ekstraksi
   = makin ASAM. Manis datang dari ekstraksi yang cukup
3. **Level sangrai ga masuk daftar** padahal sinyal paling kuat. Sudah ditambah jadi Langkah 6

### Rasio & Golden Cup — koreksi penting
- **SCA Golden Cup: rasio 55 g/L (≈1:18), toleransi ±10% → ±1:16,5 s/d 1:20.** Suhu 93±3 °C (90–96)
- **TDS 1,15–1,35%** (kekuatan) dan **extraction yield 18–22%** — DUA UKURAN BEDA, sering ketuker
- **Rasio ga nentuin extraction, rasio nentuin kekuatan.** Extraction diatur gilingan/suhu/waktu/agitasi
- **1:15 = 66,7 g/L → DI LUAR rentang SCA** (lebih pekat). 1:15 itu konvensi praktisi, bukan standar SCA.
  Riset SCAE: orang Eropa suka lebih pekat, sampai ±1,45–1,50% TDS — dari sini asal angka 1,45 Dustin
- ⚠️ **Jebakan nama "TDS":** TDS air (100–150 ppm, sebelum seduh) vs TDS seduhan (1,25% = 12.500 ppm).
  Beda ±100×. Selalu sebut yang mana
- ⚠️ **KOREKSI PENTING — resep Hoffmann.** "The Ultimate V60 Technique" (YouTube 2020) itu
  **30 g : 500 g = 1:16,7**, BUKAN 1:15. Banyak blog salah kutip jadi 1:15 (kemungkinan ketuker sama
  penanda waktu "1:15" di resepnya). Selalu pakai 1:16,7
- Asal-usul populernya 1:15: angkanya bulat & gampang diinget (15 g → 225 g), plus selera spesialti
  modern memang lebih pekat dari patokan lama. Bukan lahir dari riset

### Perkolasi (perjalanan air lewat bubuk)
- **Jalan pintas air** (istilah teknisnya channeling) = penjelasan kenapa kopi bisa **asam DAN pahit
  barengan**. Jalur yang dilewati terus-terusan jadi kelewat (pahit), bubuk yang cuma kena sedikit air
  jadi kurang (asam). Dua-duanya ketumpuk di satu cangkir. Ini sudut paling relatable buat konten
- Bubuk dengan ukuran campur aduk (banyak halus + banyak kasar) **lebih gampang bikin jalan pintas**
  dibanding bubuk yang seragam
- ⚠️ **KONTRA-INTUITIF & kuat buat konten:** menurut Gagné, **aliran yang terlalu lambat justru bikin
  air lebih susah nyebar rata** di dalam bubuk. Jadi "nuang selambat mungkin" bukan otomatis lebih baik
- Menurut Gagné juga: seduhan sebaiknya baru benar-benar mulai **setelah seluruh bubuk basah merata**;
  dan pakai gilingan dengan sebaran ukuran yang lebih seragam
- **Bypass** (definisi Gagné): air yang berhasil lewat mengitari bubuk dan **ga ikut mengekstrak**
- **Schmieder dkk. (2023)**, *Foods* 12(15):2871 — **kecepatan alir = variabel PALING dominan**
- Bubuk nempel kering di dinding kertas = bubuk yang ga pernah kena air. Perbaikan gratis: putar pelan
  dripper setelah tuangan terakhir
- ⚠️ Aku **belum berhasil memverifikasi isi keempat "Four Rules"** Gagné satu per satu lewat pencarian.
  Artikelnya dipakai sebagai sumber, tapi **jangan sebut "rule nomor sekian bilang X"**
- Sumber: Schmieder dkk. (2023) · Moroney dkk. (2015, Hukum Darcy) · Sano dkk. (2019) · Ahmed dkk. (2019) ·
  Gagné "The Four Rules of Optimal Coffee Percolation" (2021) & "Extraction Uniformity and Channeling" (2019)

### Cut brew
- ⚠️ **"Cut brew" BUKAN istilah baku** di literatur kopi — ga ketemu di sumber Inggris maupun Indonesia.
  Yang terdokumentasi itu prinsipnya (motong ekor ekstraksi) dan teknik sepupunya (**bypass**).
  Karena itu carousel-nya wajib mendefinisikan istilahnya dulu di slide 2
- **Urutan kelarutan** (BUKTI KUAT): awal = asam + aroma paling larut · tengah = gula, karamel,
  melanoidin · akhir = senyawa pahit berat + fenolik yang bikin kering/astringen
- ⚠️ **Anggapan "awal selalu bagus, akhir selalu jelek" itu penyederhanaan.** Sumber edukasi roaster
  justru menyebut cangkir bagus butuh **lengkung penuh** — potong kepagian = asam dan tipis
- **Bypass** = tambah air panas langsung ke cangkir setelah seduhan. Terdokumentasi, dipakai di
  kompetisi, dan **sempat begitu dominan di World AeroPress Championship sampai akhirnya dilarang**
- ⚠️ **JANGAN pakai angka "sweetness naik 22%, astringency turun 35%"** yang beredar di internet.
  Ketemunya cuma di satu blog (Coffee On Cue) tanpa nama studi. Tidak terverifikasi
- Sumber: Moroney dkk. (2015) · Wang & Lim (2021) · Gagné "The Four Rules of Optimal Coffee
  Percolation" (Coffee ad Astra) · Barista Hustle IM 2.06 · Perfect Daily Grind (2024) soal bypass
- **Bahasa:** sebut cut brew sebagai **"teknik"**, jangan "alat". Permintaan Dustin
- Slide "batas/yang perlu dijaga" sudah dihapus atas permintaan Dustin. Catatan soal potong kepagian
  tetap berlaku sebagai pengetahuan internal, tapi jangan dibikin slide lagi

### Suhu ruangan / grinder & ukuran gilingan
- **Uman dkk. (2016)**, *Scientific Reports* 6:24483 (co-author **Colonna-Dashwood**) — menggiling dingin
  = sebaran partikel lebih seragam & ukuran rata-rata lebih kecil. Sebaran **tidak** dipengaruhi asal biji
- Angkanya: −196 °C = 61 μm · −79 °C = 63 μm · −19 °C = 73 μm · 20 °C = 70 μm. ⚠️ Efek dramatisnya di suhu
  kriogenik; antara freezer dan suhu ruang bedanya kecil dan **ga monoton**
- **Barista Hustle** (Æ 2.03/2.04): kopi hangat lebih **liat**, pecah jadi lebih sedikit keping → **fines
  lebih sedikit** → ekstraksi turun. Yang terdokumentasi itu **grinder panas karena dipakai terus** (ruang
  giling 80–100 °C), **bukan** suhu ruangan
- ⚠️ Digilingin lebih halus balikin **waktu alir**, TAPI **rasanya ga balik sama** — yang berubah sebarannya
- Ada efek lawan: ruangan panas → dripper lebih hangat → ekstraksi naik. Sebagian saling meniadakan

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
| *Gastrophysics: The New Science of Eating* — Charles Spence | Pengaruh suasana & ekspektasi terhadap rasa |
| *The Craft and Science of Coffee* — ed. Britta Folmer | Bacaan lanjutan — **bukan sumber angka** |

---

## 8. Catatan Kerja

- **Git:** kembangkan di branch `claude/coffee-tasting-notes-mhe48b`. PR #1 masih draft & open.
- **Cek overflow slide:** `render.js` punya mode `MEASURE=1` — render tanpa nyimpen file, cuma nge-print
  slide mana yang kepotong (`h > 1351` atau foot lewat 1281px). Jalankan tiap habis nulis slide baru,
  jauh lebih cepat daripada ngeliatin satu-satu.
- **Automation:** langganan PR activity & check-in terjadwal **sudah dimatikan** atas permintaan
  Dustin. Jangan dihidupkan lagi tanpa diminta.
- **Environment:** WebFetch diblokir egress — hanya WebSearch yang jalan. LibreOffice tidak bisa
  memuat docx, jadi verifikasi dokumen lewat isi XML, bukan render PDF.
- **Kebiasaan Dustin:** dia menghargai koreksi faktual. Sudah dua kali terselamatkan dari salah
  fatal — gelar "World" vs "Indonesia" Barista Champion, dan kalsium vs magnesium.
  **Selalu cek klaimnya sebelum dibuatkan konten.**
