import tweepy
import datetime
import os

# Twitter API bilgilerini ortam değişkenlerinden al
api_key = os.environ["TWITTER_API_KEY"]
api_secret = os.environ["TWITTER_API_SECRET"]
access_token = os.environ["TWITTER_ACCESS_TOKEN"]
access_token_secret = os.environ["TWITTER_ACCESS_TOKEN_SECRET"]

# Twitter API bağlantısı kur
auth = tweepy.OAuth1UserHandler(api_key, api_secret, access_token, access_token_secret)
api = tweepy.API(auth)

# Hedef tarih: 2 Temmuz 2028 saat 16:30
target = datetime.datetime(2028, 7, 2, 16, 30)
now = datetime.datetime.now()
delta_days = (target - now).days

# Tweet içeriği
if delta_days > 0:
    tweet = f"{delta_days} gün kaldı."
elif delta_days == 0:
    tweet = "Bugün!"
else:
    tweet = "Etkinlik geçti."

# Tweet gönder
api.update_status(tweet)
