# 🌿 TUGAS MANDIRI 6: ADA BACKTRACKING (DFS MAZE SOLVER)

Aplikasi sederhana ini dibuat untuk memenuhi Tugas Mandiri 6 mata kuliah Analisis Desain Algoritma Pemrograman (ADA). Sistem ini berfokus pada penyelesaian masalah labirin (Maze) menggunakan algoritma Depth First Search (DFS) dengan teknik Backtracking.

<div align="center">
  <img src="https://drive.google.com/uc?export=view&id=1Dm2JYvBbVpMS7ZOoEzkaCZeU2NV-jsiq" alt="Maze Solver Animation" width="600"/>
</div>

## 👥 IDENTITAS
- **Nama**: Muhammad Arif Wicaksono
- **NPM**: 2410631170034
- **Kelas**: 4A Informatika

## 🚀 STATUS & FITUR PROYEK
> **Important**
> Aplikasi ini adalah versi web interaktif dari program penyelesaian labirin yang awalnya berjalan di CLI/Terminal.

1. **Maze Draw (Penggambaran Labirin)**: Memvisualisasikan matriks labirin 11x13 ke dalam bentuk grafis.
2. **State Space Tree (Pohon Ruang Status)**: Menampilkan visualisasi pohon dari langkah-langkah DFS.
3. **DFS Simulator (Simulasi Backtracking)**: Menyimulasikan proses pencarian jalur keluar (S ke F) secara *real-time* dengan penandaan warna untuk node yang sedang dikunjungi dan node yang di-*backtrack*.

## 🛠️ PANDUAN INSTALASI LOKAL

**Prasyarat**
Pastikan Anda sudah menginstal Python 3.8 - 3.11 di komputer Anda.

1️⃣ **Clone Repository**
```bash
git clone https://github.com/Rif340/TugasMandiri6_ADA_Backtracking.git
cd TugasMandiri6_ADA_Backtracking
```

2️⃣ **Install Dependensi**
Instal pustaka-pustaka Python yang dibutuhkan:
```bash
pip install -r requirements.txt
```

3️⃣ **Jalankan Aplikasi**
Mulai server lokal Streamlit Anda dengan perintah:
```bash
streamlit run app.py
```
Aplikasi akan otomatis terbuka di browser Anda pada alamat `http://localhost:8501`.

## 💻 TECH STACK
- Python 3 (Logika & Algoritma Utama)
- Streamlit (Framework Web UI)
- Matplotlib (Visualisasi Grafis)
