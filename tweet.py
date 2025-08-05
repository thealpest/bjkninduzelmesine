import os
import tweepy
from datetime import datetime
from dateutil.relativedelta import relativedelta

# Twitter API kimlik bilgileri
client = tweepy.Client(
    consumer_key=os.environ["CONSUMER_KEY"],
    consumer_secret=os.environ["CONSUMER_SECRET"],
    access_token=os.environ["ACCESS_TOKEN"],
    access_token_secret=os.environ["ACCESS_TOKEN_SECRET"],
    bearer_token=os.environ["BEARER_TOKEN"],
)

# Şu anki zaman ve hedef tarih
now = datetime.now()
deadline = datetime(2028, 7, 2, 16, 30)

# Zaman farkı
delta = relativedelta(deadline, now)
total_days = (deadline - now).days

# Çok satırlı tweet metni
tweet = f"""{delta.years} yıl
{delta.months} ay
{delta.days} gün kaldı."""

# Tweet gönder
response = client.create_tweet(text=tweet)
print("Tweet atıldı. Tweet ID:", response.data["id"])
