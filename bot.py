import os
import time
import requests
from datetime import datetime
import pytz

BOT_TOKEN = os.getenv("BOT_TOKEN")
GROUP_IDS = [os.getenv("GROUP_ID_1"), os.getenv("GROUP_ID_2")]

timezone = pytz.timezone("Asia/Karachi")

def send(msg):
    for chat_id in GROUP_IDS:
        requests.post(
            f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage",
            data={"chat_id": chat_id, "text": msg}
        )

def run():
    while True:
        now = datetime.now(timezone).strftime("%H:%M")
        
        for i in range(1, 4):
            msg = os.getenv(f"MSG_{i}")
            t = os.getenv(f"TIME_{i}")
            
            if msg and t == now:
                send(msg)
                time.sleep(60)

        time.sleep(1)

run()
