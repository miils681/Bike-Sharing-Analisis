# Bike Sharing Dashboard

Bike Sharing Dashboard adalah dashboard visualisasi data berbasis Streamlit yang menyediakan analisis mengenai penyewaan sepeda yang menggunakan Bike Sharing Dataset (https://www.kaggle.com/datasets/lakshmi25npathi/bike-sharing-dataset). Dashboardd ini menampilkan beberapa analisis seperti tren penyewaan sepeda berdasarkan jam, kondisi cuaca, pengguna (casual dan registered), serta tren berdasarkan hari kerja atau libur.

 Anda bisa melakukan filter data berdasarkan jam dan tanggal, serta menampilkan visualisasi data berupa tabel dan grafik penyewaan sepeda.

## Fitur Utama
- **Penyewaan Sepeda Berdasarkan Jam**: Menampilkan waktu paling populer dalam penyewaan sepeda.
- **Pengaruh Cuaca terhadap Penyewaan**: Memvisualisasikan bagaimana kondisi cuaca memengaruhi jumlah penyewaan sepeda.
- **Tren Penyewaan Berdasarkan Hari Kerja dan Libur**: Menampilkan perbandingan jumlah penyewaan pada hari kerja dan hari libur.
- **Perbandingan Pengguna Casual dan Registered**: Menampilkan perbandingan penyewaan sepeda oleh pengguna casual dan registered.
- **Analisis Lanjutan**:
  - **Clustering Berdasarkan Waktu**: Mengelompokkan waktu ke dalam beberapa kategori seperti Malam, Pagi, Siang, dan Sore berdasarkan kolom `hr`. Pengelompokkannya yaitu : Malam (0-6), Pagi (6-12), Siang (12-18), dan Sore (18-24).
  - **Filter Data**: Pengguna dapat memfilter data berdasarkan jam dan tanggal tertentu untuk melihat penyewaan sepeda secara lebih spesidfik.

## Persyaratan Sistem

Pastikan Anda memiliki beberapa library Python yang dibutuhkan untuk menjalankan aplikasi ini. Anda dapat menginstalnya dengan menjalankan perintah berikut di terminal:

```bash
pip install -r requirements.txt
```

Daftar library yang dibutuhkan terdapat dalam berkas `requirements.txt`.

## Cara Menjalankan Aplikasi

1. **Clone repositori atau unduh berkas.**
2. **Pastikan Python dan Streamlit sudah terinstal.**
   - Untuk menginstal Streamlit, jalankan perintah berikut:
     ```bash
     pip install streamlit
     ```
3. **Jalankan aplikasi dengan perintah:**
   ```bash
   streamlit run dashboard/dashboard.py
   ```
   Pastikan Anda berada di direktori yang sama dengan berkas `dashboard/dashboard.py` saat menjalankan perintah ini.
   
4. **Aplikasi akan terbuka di browser** dan Anda dapat melihat visualisasi data penyewaan sepeda.

## Struktur Berkas

- `data` : Berisi dataset yang digunakan dalam analisis data.
- `Proyek_Analisis_Data.ipynb` : Berisi insight dari analisis mulai dari Gathering Data sampai Explanatory Analysiss.
- `dashboard/dashboard.py`: Berisi kode untuk menjalankan dashboard Streamlit (Bike Sharing Dashboard).
- `requirements.txt`: Berisi daftar library Python yang diperlukan untuk menjalankan aplikasi.
- `url.txt` : Berisi tautan untuk dashboard.
- `README.md`: Berisi dokumentasi ini.

## Dataset

Aplikasi ini menggunakan dua dataset:
- **hour.csv**: Dataset yang berisi data penyewaan sepeda berdasarkan jam.
- **day.csv**: Dataset yang berisi data penyewaan sepeda berdasarkan hari.
