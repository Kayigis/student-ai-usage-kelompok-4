# Analisis Student AI Usage - Kelompok 4

Repository ini berisi hasil pengerjaan post test Praktikum Algoritma dan Pemrograman 2026 untuk Kelas F, Kelompok 4. Dataset yang digunakan adalah `Student AI Usage`, dengan fokus analisis pada hubungan penggunaan AI, jam belajar, nilai akademik, screen time, dan umur responden.

## Isi Repository

```txt
.
├── README.md
├── post_test_kelompok_4.py
├── requirements.txt
├── caption_infografis_kelompok_4.txt
├── data/
│   └── Kelas F_Student AI Usage.csv
└── hasil_kelompok_4/
    ├── 01_kategori_a_median_grades_before.png
    ├── 02_kategori_b_homework_under_2_hours.png
    ├── 03_kategori_c_correlation_heatmap.png
    └── 04_kategori_d_age_distribution.png
```

## Penjelasan File

`post_test_kelompok_4.py` adalah source code utama untuk membaca dataset, melakukan analisis, dan menghasilkan 4 grafik sesuai soal Kelompok 4.

`data/Kelas F_Student AI Usage.csv` adalah dataset utama yang digunakan dalam analisis. Dataset berisi 100 data responden dengan kolom umur, jenjang pendidikan, jam belajar, status penggunaan AI, tools AI, tujuan penggunaan AI, nilai sebelum AI, nilai setelah AI, dan screen time harian.

`hasil_kelompok_4/` adalah folder output yang berisi gambar hasil visualisasi. Semua gambar di folder ini dihasilkan langsung dari script Python.

`caption_infografis_kelompok_4.txt` berisi caption atau insight singkat untuk membantu menjelaskan masing-masing grafik pada infografis.

`requirements.txt` berisi daftar library Python yang diperlukan untuk menjalankan script.

## Soal Kelompok 4

Kelompok 4 mengerjakan 4 kategori berikut:

1. Kategori A: Menentukan median `grades_before_ai` berdasarkan `education_level`, lalu menampilkan hasilnya dalam Bar Chart.
2. Kategori B: Mencari siswa yang menggunakan AI untuk `Homework` dengan waktu belajar mandiri kurang dari 2 jam, lalu menampilkan hasilnya dalam Bar Chart.
3. Kategori C: Menghitung matriks korelasi antar kolom numerik, lalu menampilkan hasilnya dalam Heatmap.
4. Kategori D: Menampilkan distribusi umur siswa dalam Histogram atau grafik distribusi frekuensi.

## Hasil Visualisasi

### 1. Kategori A - Median Nilai Awal Berdasarkan Jenjang Pendidikan

![Kategori A](hasil_kelompok_4/01_kategori_a_median_grades_before.png)

Grafik ini menunjukkan median nilai awal sebelum penggunaan AI berdasarkan jenjang pendidikan. Median nilai siswa `school` adalah 64.5, sedangkan `college` adalah 63.0. Selisihnya kecil, sehingga kemampuan awal kedua kelompok dapat dianggap relatif seimbang.

### 2. Kategori B - Pengguna AI untuk Homework dengan Jam Belajar < 2 Jam

![Kategori B](hasil_kelompok_4/02_kategori_b_homework_under_2_hours.png)

Grafik ini menampilkan siswa yang menggunakan AI untuk membantu mengerjakan homework dengan waktu belajar mandiri kurang dari 2 jam per hari. Terdapat 6 siswa yang memenuhi kriteria ini, dan seluruhnya mengalami peningkatan nilai setelah menggunakan AI.

### 3. Kategori C - Heatmap Korelasi Kolom Numerik

![Kategori C](hasil_kelompok_4/03_kategori_c_correlation_heatmap.png)

Heatmap ini menunjukkan hubungan antar variabel numerik, yaitu umur, jam belajar, nilai sebelum AI, nilai setelah AI, dan screen time harian. Korelasi terkuat terlihat antara nilai sebelum AI dan nilai setelah AI, dengan nilai korelasi sekitar 0.76.

### 4. Kategori D - Distribusi Umur Siswa

![Kategori D](hasil_kelompok_4/04_kategori_d_age_distribution.png)

Grafik ini menunjukkan sebaran umur responden. Umur responden berada pada rentang 14 sampai 19 tahun, dengan jumlah responden terbanyak pada usia 15 tahun.

## Cara Menjalankan Script

Pastikan Python 3 sudah tersedia, lalu jalankan perintah berikut dari root repository:

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python post_test_kelompok_4.py
```

Jika perintah `python` tidak tersedia di sistem, gunakan:

```bash
python3 post_test_kelompok_4.py
```

Setelah script dijalankan, gambar akan dibuat ulang di folder:

```txt
hasil_kelompok_4/
```

## Ringkasan Insight

Analisis menunjukkan bahwa nilai awal siswa pada jenjang `school` dan `college` relatif mirip. Pada kelompok siswa yang menggunakan AI untuk homework dengan jam belajar rendah, seluruh siswa mengalami peningkatan nilai. Korelasi paling kuat ditemukan antara nilai sebelum dan sesudah penggunaan AI, sedangkan variabel seperti screen time dan durasi belajar memiliki korelasi yang lebih lemah terhadap nilai akademik.
