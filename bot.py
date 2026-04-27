import os
import time
import requests
from datetime import datetime
import pytz

# 🔹 BOT TOKEN
BOT_TOKEN = os.getenv("BOT_TOKEN")

# 🔹 GROUP IDS (1–20 manual)
GROUP_IDS = [gid for gid in [
    os.getenv("GROUP_ID_1"),
    os.getenv("GROUP_ID_2"),
    os.getenv("GROUP_ID_3"),
    os.getenv("GROUP_ID_4"),
    os.getenv("GROUP_ID_5"),
    os.getenv("GROUP_ID_6"),
    os.getenv("GROUP_ID_7"),
    os.getenv("GROUP_ID_8"),
    os.getenv("GROUP_ID_9"),
    os.getenv("GROUP_ID_10"),
    os.getenv("GROUP_ID_11"),
    os.getenv("GROUP_ID_12"),
    os.getenv("GROUP_ID_13"),
    os.getenv("GROUP_ID_14"),
    os.getenv("GROUP_ID_15"),
    os.getenv("GROUP_ID_16"),
    os.getenv("GROUP_ID_17"),
    os.getenv("GROUP_ID_18"),
    os.getenv("GROUP_ID_19"),
    os.getenv("GROUP_ID_20"),
] if gid]

# 🔹 Pakistan timezone
timezone = pytz.timezone("Asia/Karachi")

# 🔹 Send message function
def send(msg):
    for chat_id in GROUP_IDS:
        try:
            requests.post(
                f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage",
                data={"chat_id": chat_id, "text": msg}
            )
        except Exception as e:
            print("Error sending:", e)

# 🔹 Main loop (unlimited MSG/TIME support)
def run():
    while True:
        now = datetime.now(timezone).strftime("%H:%M")

        i = 1
        while True:
            msg = os.getenv(f"MSG_{i}")
            t = os.getenv(f"TIME_{i}")

            # stop when no more variables
            if not msg or not t:
                break

            if t == now:
                print(f"Sending MSG_{i} at {now}")
                send(msg)
                time.sleep(60)  # prevent duplicate sends

            i += 1

        time.sleep(1)

# 🔹 Start bot
run()
