import time
import random
import requests
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.proxy import Proxy, ProxyType
from selenium.webdriver.chrome.options import Options

# 🔥 Ambil proxy dari proxyscrape
def get_proxy():
    url = "https://api.proxyscrape.com/v2/?request=getproxies&protocol=http&timeout=1000&country=all"
    response = requests.get(url)
    proxies = response.text.split("\n")
    return random.choice(proxies).strip()

# 🔥 Setup Selenium dengan proxy
def setup_driver(proxy):
    chrome_options = Options()
    chrome_options.add_argument("--headless")  # Biar jalan di background
    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument(f"--proxy-server={proxy}")

    service = Service("/usr/bin/chromedriver")  # Sesuaikan path chromedriver kamu
    driver = webdriver.Chrome(service=service, options=chrome_options)
    return driver

# 🔥 Jalankan bot
def start_trial():
    proxy = get_proxy()
    print(f"[+] Menggunakan Proxy: {proxy}")

    try:
        driver = setup_driver(proxy)
        driver.get("https://app.apponfly.com/trial")
        time.sleep(5)

        # Klik tombol Start
        start_button = driver.find_element(By.XPATH, "//button[contains(text(), 'Start')]")
        start_button.click()
        time.sleep(10)

        # Buka YouTube di browser trial
        youtube_url = "https://www.youtube.com/watch?v=3oTxP-a0rnE"  # Ganti dengan link YouTube kamu
        driver.get(youtube_url)
        time.sleep(600)  # Biarkan 10 menit biar dihitung view

        driver.quit()
        print("[+] Trial selesai, siap ulangi!")

    except Exception as e:
        print(f"[-] Error: {e}")
        driver.quit()

# 🔥 Looping biar otomatis restart setiap trial habis
while True:
    start_trial()
    time.sleep(60)  # Tunggu sebentar sebelum ulangi
