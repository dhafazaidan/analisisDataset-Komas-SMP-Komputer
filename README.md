# 📊 Analisis Dataset: Proporsi SMP Memiliki Fasilitas Komputer (UTS Komputer & Masyarakat)

Proyek ini merupakan bagian dari **Ujian Tengah Semester (UTS)** untuk mata kuliah **Komputer & Masyarakat** di **Universitas Singaperbangsa Karawang (UNSIKA)**.  
Analisis dilakukan terhadap dataset resmi dari portal **[data.go.id](https://data.go.id)** yang berjudul:

> **Proporsi SMP yang Memiliki Fasilitas Komputer untuk Tujuan Pengajaran – SMP/MTs/Sederajat (2024)**

Proyek ini menggunakan **Python** sebagai alat analisis data untuk mengolah, memvisualisasikan, dan menginterpretasikan hasil statistik yang berkaitan dengan pemerataan akses teknologi pendidikan di Indonesia.

---

## 🧭 Tujuan Proyek

1. Mengidentifikasi tingkat kepemilikan fasilitas komputer di sekolah menengah pertama (SMP) di seluruh provinsi Indonesia.  
2. Membandingkan proporsi antara **sekolah negeri dan swasta**.  
3. Menunjukkan kesenjangan digital antarwilayah melalui visualisasi data.  
4. Menyusun analisis deskriptif dan kesimpulan berdasarkan hasil visualisasi.

---

## 🧩 Struktur Direktori Proyek
analisisDataset/
│
├── data/
│ └── raw/
│ └── Proporsi_SMP_komputer_2024.xlsx
│
├── reports/
│ └── figures/
│ ├── chart1_total_per_provinsi.png
│ └── chart2_negeri_vs_swasta_top10.png
│
├── scripts/
│ └── make_charts.py
│
├── src/
│ ├── analysis/
│ │ └── visualize.py
│ ├── utils/
│ │ └── io.py
│ └── main.py
│
├── .env
├── requirements.txt
└── README.md

---

## ⚙️ Teknologi yang Digunakan

| Komponen | Deskripsi |
|----------|------------|
| **Python 3.13** | Bahasa pemrograman utama |
| **pandas** | Manipulasi dan pembersihan data |
| **matplotlib** | Visualisasi grafik batang |
| **reportlab** | Pembuatan laporan PDF |
| **virtualenv / venv** | Isolasi lingkungan proyek |
| **dotenv** | Manajemen variabel lingkungan (.env) |

---

## 🚀 Cara Menjalankan Proyek

1. **Kloning repositori ini:**
   ```bash
    git clone https://github.com/USERNAME/analisisDataset-SMP-Komputer.git
    cd analisisDataset-SMP-Komputer
   ```
2. Buat dan aktifkan virtual environment:
   ```bash
    python -m venv .venv
    .\.venv\Scripts\Activate.ps1     # Windows PowerShell
    source .venv/bin/activate        # Linux/Mac
   ```
4. Instal dependensi:
   ```bash
    pip install -r requirements.txt
   ```
6. Jalankan program utama:
   ```bash
    python -m src.main
   ```
8. Hasil:
   - Dua grafik otomatis tersimpan di folder reports/figures/.
   - Laporan akhir otomatis dihasilkan dalam format PDF:
     Laporan_UTS_Komputer_Masyarakat_Analisis_Dataset.pdf

---

### 👤 Penulis

Nama: Dhafa Zaidan Ahnaf

NPM: 2310631170073

Program Studi: Informatika, Universitas Singaperbangsa Karawang

Mata Kuliah: Komputer & Masyarakat

Dosen Pengampu: Rini Mayasari, M.kom

---

### 🔗 Repositori

**[📦 GitHub Repository]([https://github.com/dhafazaidan/analisisDataset-Komas-SMP-Komputer])**




