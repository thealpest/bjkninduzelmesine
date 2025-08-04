import os
from datetime import datetime, timedelta, timezone
import tweepy
from dateutil.relativedelta import relativedelta

# Twitter API kimlik bilgileri ve Bearer Token
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

# Geri sayım tarihi (2 Temmuz 2028, 16:30 GMT+3)
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

    # Satır satır tweet oluştur
    lines = []
    if years > 0:
        lines.append(f"{years} YIL")
    if months > 0:
        lines.append(f"{months} AY")
    if days > 0:
        lines.append(f"{days} GÜN kaldı ⏳")
    else:
        # Eğer sadece yıl ve ay varsa ve gün 0 ise "0 GÜN kaldı." yazabiliriz
        lines.append("0 GÜN kaldı.")

    lines.append("")  # Boş satır
    lines.append(f"({total_days} gün)")

    tweet = "\n".join(lines)

try:
    response = client.create_tweet(text=tweet)
    print("Tweet atıldı. Tweet ID:", response.data["id"])
except Exception as e:
    print("Tweet gönderilirken hata oluştu:", e)
