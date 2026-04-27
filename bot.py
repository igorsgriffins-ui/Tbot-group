import os
import time
import requests
from datetime import datetime
import pytz

BOT_TOKEN = os.getenv("BOT_TOKEN")

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
] if gid]

timezone = pytz.timezone("Asia/Karachi")

sent_today = {}

def send(msg):
    for chat_id in GROUP_IDS:
        try:
            requests.post(
                f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage",
                data={"chat_id": chat_id, "text": msg}
            )
            time.sleep(0.5)
        except Exception as e:
            print("Error:", e)

def run():
    global sent_today

    while True:
        now_dt = datetime.now(timezone)
        now_time = now_dt.strftime("%H:%M")
        today = now_dt.strftime("%Y-%m-%d")

        if sent_today.get("date") != today:
            sent_today = {"date": today}

        # 🔥 scan 1–100 (you can increase)
        for i in range(1, 101):
            msg = os.getenv(f"MSG_{i}")
            t = os.getenv(f"TIME_{i}")

            if not msg or not t:
                continue  # skip missing numbers

            key = f"{today}_{i}"

            if t == now_time and key not in sent_today:
                print(f"Sending MSG_{i} at {now_time}")
                send(msg)
                sent_today[key] = True

        time.sleep(10)

run()
