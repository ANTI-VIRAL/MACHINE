import requests
import time
import os
from dotenv import load_dotenv

# Load API Key dari .env
load_dotenv()
API_KEY = os.getenv("API_KEY")
API_SECRET = os.getenv("API_SECRET")

# Konfigurasi
TRADING_PAIR = "VRSC_USDT"
TARGET_PRICE = 5.0  # Harga target jual
BASE_URL = "https://safetrade.exchange/api/v2/peatio"

def get_price():
    """Mengambil harga terbaru VRSC/USDT"""
    url = f"{BASE_URL}/public/markets/{TRADING_PAIR}/tickers"
    response = requests.get(url).json()
    return float(response["ticker"]["last"])

def get_balance():
    """Mengambil saldo VRSC"""
    url = f"{BASE_URL}/account/balances"
    headers = {"X-Auth-Apikey": API_KEY, "X-Auth-Nonce": API_SECRET}
    response = requests.get(url, headers=headers).json()
    
    for asset in response:
        if asset["currency"] == "vrsc":
            return float(asset["balance"])
    return 0

def sell_verus(amount):
    """Menjual seluruh saldo VRSC"""
    url = f"{BASE_URL}/market/orders"
    headers = {"X-Auth-Apikey": API_KEY, "X-Auth-Nonce": API_SECRET}
    data = {
        "market": TRADING_PAIR.lower(),
        "side": "sell",
        "volume": str(amount),
        "ord_type": "market"
    }
    response = requests.post(url, headers=headers, json=data)
    return response.json()

# Loop cek harga & jual jika tembus target
while True:
    try:
        price = get_price()
        print(f"Harga VRSC sekarang: ${price}")

        if price >= TARGET_PRICE:
            print("Harga tembus $5! Menjual seluruh VRSC...")
            balance = get_balance()
            if balance > 0:
                sell_response = sell_verus(balance)
                print("Respon jual:", sell_response)
            else:
                print("Saldo VRSC kosong!")
            break  # Hentikan bot setelah jual

    except Exception as e:
        print("Error:", e)

    time.sleep(60)  # Cek harga tiap 60 detik
