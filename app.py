import requests
import time


ids = requests.get("https://hacker-news.firebaseio.com/v0/topstories.json").json()


for story_id in ids[:30]:

    data = requests.get(f"https://hacker-news.firebaseio.com/v0/item/{story_id}.json").json()

    print({"title": data.get("title"), "link": data.get("url", None)})

    # 1秒待つ（ルール）
    time.sleep(1)
