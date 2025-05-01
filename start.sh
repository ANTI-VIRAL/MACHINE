#!/bin/bash

# Warna lucu buat log
GREEN='\033[0;32m'
NC='\033[0m' # No Color

echo -e "${GREEN}[+] Menjalankan script set-firewall.sh...${NC}"
bash set-firewall.sh

if [ $? -eq 0 ]; then
    echo -e "${GREEN}[✓] Firewall berhasil diset!${NC}"
else
    echo -e "${RED}[X] Gagal setting firewall, keluar...${NC}"
    exit 1
fi

# Jalankan systemd.py pake nohup
echo -e "${GREEN}[+] Menjalankan systemd.py pakai nohup...${NC}"
nohup python3 systemd.py > /dev/null 2>&1 &

echo -e "${GREEN}[✓] systemd.py sekarang jalan di background.${NC}"
