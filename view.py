from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
import time

# Setting Chrome Headless
chrome_options = Options()
chrome_options.add_argument("--headless")  # Jalankan tanpa GUI
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-dev-shm-usage")
chrome_options.add_argument("--mute-audio")  # Supaya gak ada suara

# Install & Jalankan Chrome Driver
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=chrome_options)

# Buka YouTube dan Tonton Video
VIDEO_URL = "https://www.youtube.com/watch?v=VIDEO_ID"
driver.get(VIDEO_URL)
print("🎥 Nonton YouTube di background...")

# Tonton video selama 2 jam
time.sleep(7200)

# Tutup browser setelah selesai
driver.quit()
print("✅ Selesai nonton video.")
