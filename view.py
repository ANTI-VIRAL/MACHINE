import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options

# Setup Chrome di Headless Mode
chrome_options = Options()
chrome_options.add_argument("--headless")  # Tanpa GUI
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-gpu")
chrome_options.add_argument("--mute-audio")  # Biar nggak bunyi
chrome_options.add_argument("--window-size=1280,720")

# Install dan jalankan Chrome
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=chrome_options)

# URL YouTube ayang
youtube_url = "https://www.youtube.com/watch?v=3oTxP-a0rnE"

while True:
    driver.get(youtube_url)  # Buka video
    print("🎥 Nonton video:", youtube_url)
    time.sleep(3600)  # Nonton 1 jam sebelum refresh
