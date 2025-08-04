import os
from datetime import datetime, timedelta, timezone
import tweepy

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

# Şu anki zaman (GMT+3)
now = datetime.now(timezone(timedelta(hours=3)))

# Kalan gün sayısı
days_left = (deadline.date() - now.date()).days

# Tweet metni
if days_left > 0:
    tweet = f"{days_left} gün kaldı."
elif days_left == 0:
    tweet = "Bugün!"
else:
    tweet = "Etkinlik sona erdi."

# Tweet atma işlemi
try:
    response = client.create_tweet(text=tweet)
    print("Tweet atıldı. Tweet ID:", response.data["id"])
except Exception as e:
    print("Tweet gönderilirken hata oluştu:", e)
