import os
import time

YOUTUBE_URL = "https://www.youtube.com/watch?v=3oTxP-a0rnE"

while True:
    os.system(f"nohup yt-dlp -q -o - {YOUTUBE_URL} | ffplay -nodisp -autoexit - > /dev/null 2>&1 &")
    print("🎥 Nonton YouTube di background...")
    time.sleep(21600)  # Refresh tiap 6 jam
