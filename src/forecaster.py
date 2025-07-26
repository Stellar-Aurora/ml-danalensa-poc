import pandas as pd
import statsmodels.api as sm

def get_forecast(user_id, transaction_data):
    """
    Fungsi ini later akan menerima data transaksi seorang pengguna dan 
    mengembalikan hasil prediksi arus kas untuk 30 hari ke depan.

    TODO:
    - Lakukan preprocessing data (resampling harian/mingguan).
    - Latih model SARIMA dengan parameter yang sesuai.
    - Hasilkan prediksi.
    - Kembalikan hasil dalam format JSON.
    """
    
    # --- Logika Inti Model nanti disini  ---
    
    print(f"Memproses prediksi untuk user: {user_id}...")
    
    # Untuk sekarang, kembalikan hasil dummy
    # dummy_forecast = {"tanggal": ["2025-07-27", "2025-07-28"], "prediksi_saldo": [500000, 450000]}
    
    return dummy_forecast