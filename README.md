# Danalensa - Machine Learning Proof of Concept

Repositori ini berisi kode dan eksperimen untuk validasi *baseline model* dari proyek Danalensa, Masa depan keuanganmu, diprediksi hari ini.

## ☁ Tentang

Tujuan dari POC ini adalah untuk membuktikan kelayakan teknis dari hipotesis ide Danalensa mengenai kemampuan untuk memprediksi arus kas masa depan dari data *time-series* pendapatan tidak tetap menggunakan model SARIMA.

## 🛠️ Metodologi

Kami menggunakan pendekatan *Time-Series Forecasting* dengan algoritma **SARIMA (Seasonal AutoRegressive Integrated Moving Average)**. Model ini dilatih menggunakan dataset sintetis yang merepresentasikan tiga persona target pengguna yang merupakan seorang desainer grafis, seorang driver ojol, dan seorang penulis konten lepas.

## 📁 Struktur Folder

-   **/data:** Berisi dataset sintetis (`.csv`) yang di-generate.
-   **/notebooks:** Berisi Jupyter Notebook untuk proses Eksplorasi Data (EDA), *training*, dan evaluasi model sederhana.
-   **/src:** Berisi *script* Python untuk men-generate dataset dan fungsi *forecasting* utama.


## 📊 Hasil Awal

Eksperimen awal menunjukkan bahwa model SARIMA mampu menangkap pola musiman, terutama pada data dengan siklus mingguan yang jelas (pada percobaan Persona "Sari"), dengan MAE mencapai ~44%(akan diperbaiki kedepannya). 
Ini memvalidasi bahwa pendekatan yang dilakukan secara teknis adalah dapat diimplementasikan feasible

---
