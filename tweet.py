import os
import tweepy

# Environment variable'lardan API anahtarlarını al
consumer_key = os.environ["CONSUMER_KEY"]
consumer_secret = os.environ["CONSUMER_SECRET"]
access_token = os.environ["ACCESS_TOKEN"]
access_token_secret = os.environ["ACCESS_TOKEN_SECRET"]

# OAuth1 ile kimlik doğrulama
auth = tweepy.OAuth1UserHandler(
    consumer_key,
    consumer_secret,
    access_token,
    access_token_secret
)

api = tweepy.API(auth)

try:
    me = api.verify_credentials()
    print("Giriş başarılı:", me.screen_name)

    tweet = "Bu bir test tweetidir. #test"
    api.update_status(tweet)

    print("Tweet atıldı.")
except Exception as e:
    print("Hata oluştu:", e)
