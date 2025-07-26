import pandas as pd
import numpy as np
from datetime import date, timedelta


def generate_andi_data(user_id="andi_designer"):
    """
    Fungsi untuk men-generate data transaksi fiktif untuk persona Andi.
    """
    transactions = []
    start_date = date.today() - timedelta(days=365) # buat data 1 tahun ke belakang
    end_date = date.today()

    # Loop untuk setiap hari selama 1 tahun
    for single_date in pd.date_range(start_date, end_date):
        day = single_date.day
        weekday = single_date.weekday() # Senin=0, Minggu=6

        # --- LOGIKA PEMASUKAN ---
        
        # Pemasukan Utama (cenderung di akhir bulan)
        if day >= 25:
            # Tidak setiap hari dapat, kita buat probabilitas 30% per hari
            if np.random.choice([True, False], p=[0.3, 0.7]):
                amount = np.random.uniform(3000000, 5000000)
                transactions.append([user_id, single_date, "Pemasukan Proyek Utama", "Pemasukan", round(amount, 0)])

        # Pemasukan Kecil (cenderung di pertengahan bulan)
        if 10 <= day <= 15:
             # Probabilitas 15% per hari
            if np.random.choice([True, False], p=[0.15, 0.85]):
                amount = np.random.uniform(500000, 1000000)
                transactions.append([user_id, single_date, "Pemasukan Proyek Revisi", "Pemasukan", round(amount, 0)])
        
        # --- LOGIKA PENGELUARAN ---

        # Pengeluaran Tetap (sesuai tanggal)
        if day == 5:
            transactions.append([user_id, single_date, "Bayar Kos", "Pengeluaran", -1500000])
        if day == 10:
            transactions.append([user_id, single_date, "Bayar Internet", "Pengeluaran", -350000])
        if day == 20:
            transactions.append([user_id, single_date, "Langganan Adobe", "Pengeluaran", -800000])

        # Pengeluaran Harian (bervariasi)
        if weekday < 5: # Senin - Jumat
            daily_expense = np.random.uniform(40000, 60000)
        else: # Sabtu - Minggu
            daily_expense = np.random.uniform(100000, 200000)
        transactions.append([user_id, single_date, "Kebutuhan Harian", "Pengeluaran", round(-daily_expense, 0)])

    # Buat DataFrame dari list transaksi
    df = pd.DataFrame(transactions, columns=["user_id", "tanggal", "keterangan", "tipe", "jumlah"])
    return df



def generate_sari_data(user_id="sari_ojol"):
    """
    Fungsi untuk men-generate data transaksi fiktif untuk persona Sari.
    """
    transactions = []
    start_date = date.today() - timedelta(days=365)
    end_date = date.today()

    for single_date in pd.date_range(start_date, end_date):
        day = single_date.day
        weekday = single_date.weekday() # Senin=0, Selasa=1, ..., Minggu=6

        # --- LOGIKA PEMASUKAN ---

        # Pemasukan Utama (Harian dari Ojol)
        # Buat pendapatan dasar dulu
        daily_income = np.random.uniform(75000, 150000)
        
        # Jika akhir pekan (Jumat, Sabtu, Minggu), pendapatannya naik 50%
        if weekday >= 4: # Jumat (4), Sabtu (5), Minggu (6)
            daily_income *= 1.5
        
        transactions.append([user_id, single_date, "Pendapatan Ojek Online", "Pemasukan", round(daily_income, 0)])

        # Pemasukan Mingguan (dari Toko Online, setiap Selasa)
        if weekday == 1: # Selasa
            weekly_income = np.random.uniform(300000, 600000)
            transactions.append([user_id, single_date, "Pencairan Toko Online", "Pemasukan", round(weekly_income, 0)])

        # --- LOGIKA PENGELUARAN ---

        # Pengeluaran Tetap (sesuai tanggal)
        if day == 1:
            transactions.append([user_id, single_date, "Cicilan Motor", "Pengeluaran", -800000])
        if day == 8:
            transactions.append([user_id, single_date, "Bayar BPJS", "Pengeluaran", -50000])
        if day == 25:
            transactions.append([user_id, single_date, "Beli Pulsa & Kuota", "Pengeluaran", -150000])
            
        # Pengeluaran Operasional Harian (Bensin & Makan)
        daily_expense = np.random.uniform(50000, 70000)
        transactions.append([user_id, single_date, "Operasional Harian", "Pengeluaran", round(-daily_expense, 0)])

    # Buat DataFrame dari list transaksi
    df = pd.DataFrame(transactions, columns=["user_id", "tanggal", "keterangan", "tipe", "jumlah"])
    return df



def generate_budi_data(user_id="budi_penulis"):
    """
    Fungsi untuk men-generate data transaksi fiktif untuk persona Budi.
    """
    transactions = []
    start_date = date.today() - timedelta(days=365)
    end_date = date.today()

    for single_date in pd.date_range(start_date, end_date):
        day = single_date.day
        weekday = single_date.weekday()

        # --- LOGIKA PEMASUKAN ---

        # Pemasukan Klien A (Retainer, tiap tanggal 1 dan 15)
        if day == 1 or day == 15:
            retainer_income = np.random.uniform(1500000, 2000000)
            transactions.append([user_id, single_date, "Pembayaran Retainer Klien A", "Pemasukan", round(retainer_income, 0)])

        # Pemasukan Klien B (Proyek Satuan, acak)
        # Kita asumsikan ada sekitar 4-5 proyek per bulan (probabilitas ~20% di hari kerja)
        if weekday < 5: # Hanya terjadi di hari kerja
            if np.random.choice([True, False], p=[0.2, 0.8]):
                project_income = np.random.uniform(200000, 400000)
                transactions.append([user_id, single_date, "Pembayaran Proyek Klien B", "Pemasukan", round(project_income, 0)])

        # --- LOGIKA PENGELUARAN ---

        # Pengeluaran Tetap (sesuai tanggal)
        if day == 3:
            transactions.append([user_id, single_date, "Bayar Kontrakan", "Pengeluaran", -1000000])
        if day == 20:
            transactions.append([user_id, single_date, "Bayar Listrik", "Pengeluaran", -200000])
            transactions.append([user_id, single_date, "Bayar WiFi", "Pengeluaran", -300000])
            
        # Pengeluaran Harian (relatif stabil)
        daily_expense = np.random.uniform(60000, 80000)
        transactions.append([user_id, single_date, "Kebutuhan Harian", "Pengeluaran", round(-daily_expense, 0)])

    # Buat DataFrame dari list transaksi
    df = pd.DataFrame(transactions, columns=["user_id", "tanggal", "keterangan", "tipe", "jumlah"])
    return df




if __name__ == "__main__":
    print("Membuat dataset untuk Persona 1: Andi...")
    andi_df = generate_andi_data()
    
    print("Membuat dataset untuk Persona 2: Sari...")
    sari_df = generate_sari_data()

    print("Membuat dataset untuk Persona 3: Budi...")
    budi_df = generate_budi_data()
    
    # Gabungkan semua data dari tiga persona
    final_df = pd.concat([andi_df, sari_df, budi_df])

    # Pastikan data diurutkan berdasarkan tanggal
    final_df = final_df.sort_values(by=["user_id", "tanggal"])

    # Simpan ke satu file CSV besar
    final_df.to_csv("../data/synthetic_transactions.csv", index=False)
    print("\nDataset gabungan untuk 3 persona berhasil dibuat!")
    print(f"File tersimpan di 'data/synthetic_transactions.csv'")
    print(f"Total {len(final_df)} transaksi berhasil di-generate.")