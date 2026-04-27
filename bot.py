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

# 🔹 Track sent messages (avoid duplicates)
sent_today = {}

# 🔹 Send message function
def send(msg):
    for chat_id in GROUP_IDS:
        try:
            requests.post(
                f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage",
                data={"chat_id": chat_id, "text": msg}
            )
            time.sleep(0.5)  # anti-spam delay
        except Exception as e:
            print("Error sending:", e)

# 🔹 Main loop (FIXED scheduling)
def run():
    global sent_today

    while True:
        now_dt = datetime.now(timezone)
        now_time = now_dt.strftime("%H:%M")
        today = now_dt.strftime("%Y-%m-%d")

        # reset daily tracking
        if "date" not in sent_today or sent_today.get("date") != today:
            sent_today = {"date": today}

        i = 1
        while True:
            msg = os.getenv(f"MSG_{i}")
            t = os.getenv(f"TIME_{i}")

            if not msg or not t:
                break

            key = f"{today}_{i}"

            # 🔥 FIX: allow 1-minute window instead of exact match
            if t == now_time and key not in sent_today:
                print(f"Sending MSG_{i} at {now_time}")
                send(msg)
                sent_today[key] = True

            i += 1

        time.sleep(10)  # check every 10 sec (stable)

# 🔹 Start bot
run()
