import os
import tweepy

# Ortam değişkenlerinden al
bearer_token = os.environ["BEARER_TOKEN"]
consumer_key = os.environ["CONSUMER_KEY"]
consumer_secret = os.environ["CONSUMER_SECRET"]
access_token = os.environ["ACCESS_TOKEN"]
access_token_secret = os.environ["ACCESS_TOKEN_SECRET"]

# V2 Client ile tweet at
client = tweepy.Client(
    bearer_token=bearer_token,
    consumer_key=consumer_key,
    consumer_secret=consumer_secret,
    access_token=access_token,
    access_token_secret=access_token_secret
)

try:
    response = client.create_tweet(text="Bu bir V2 test tweetidir. #test")
    print("Tweet atıldı. Tweet ID:", response.data["id"])
except Exception as e:
    print("Hata oluştu:", e)
