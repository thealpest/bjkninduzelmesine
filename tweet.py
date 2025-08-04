import os
import tweepy

# V2 Auth (Bearer Token + OAuth2)
client = tweepy.Client(
    bearer_token=os.environ["BEARER_TOKEN"],
    consumer_key=os.environ["CONSUMER_KEY"],
    consumer_secret=os.environ["CONSUMER_SECRET"],
    access_token=os.environ["ACCESS_TOKEN"],
    access_token_secret=os.environ["ACCESS_TOKEN_SECRET"]
)

try:
    tweet = "Bu bir test tweetidir. #v2test"
    response = client.create_tweet(text=tweet)
    print("Tweet atıldı. Tweet ID:", response.data["id"])
except Exception as e:
    print("Hata oluştu:", e)
