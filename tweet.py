import os
from datetime import datetime, timedelta, timezone
import tweepy
from dateutil.relativedelta import relativedelta

# Twitter API kimlik bilgileri
bearer_token = os.environ["BEARER_TOKEN"]
consumer_key = os.environ["CONSUMER_KEY"]
consumer_secret = os.environ["CONSUMER_SECRET"]
access_token = os.environ["ACCESS_TOKEN"]
access_token_secret = os.environ["ACCESS_TOKEN_SECRET"]

# Tweepy Client (v2 API)
client = tweepy.Client(
    bearer_token=bearer_token,
    consumer_key=consumer_key,
    consumer_secret=consumer_secret,
    access_token=access_token,
    access_token_secret=access_token_secret
)

# Hedef tarih: 2 Temmuz 2028, saat 16:30 (GMT+3)
deadline = datetime(2028, 7, 2, 16, 30, tzinfo=timezone(timedelta(hours=3)))
now = datetime.now(timezone(timedelta(hours=3)))

if now > deadline:
    tweet = "Etkinlik sona erdi."
else:
    diff = relativedelta(deadline, now)
    total_days = (deadline.date() - now.date()).days

    years = diff.years
    months = diff.months
    days = diff.days

    # Satırları oluştur
    lines = []
    if years > 0:
        lines.append(f"{years} YIL")
    if months > 0:
        lines.append(f"{months} AY")
    if days > 0:
        lines.append(f"{days} GÜN kaldı.")
    else:
        lines.append("0 GÜN kaldı.")

    lines.append("⏳")
    lines.append(f"({total_days} gün)")

    tweet = "\n".join(lines)

try:
    response = client.create_tweet(text=tweet)
    print("Tweet atıldı. Tweet ID:", response.data["id"])
except Exception as e:
    print("Tweet gönderilirken hata oluştu:", e)
