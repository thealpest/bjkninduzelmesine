import os
import tweepy

consumer_key = os.environ["TWITTER_CONSUMER_KEY"]
consumer_secret = os.environ["TWITTER_CONSUMER_SECRET"]
access_token = os.environ["TWITTER_ACCESS_TOKEN"]
access_token_secret = os.environ["TWITTER_ACCESS_TOKEN_SECRET"]

auth = tweepy.OAuth1UserHandler(consumer_key, consumer_secret, access_token, access_token_secret)
api = tweepy.API(auth)

try:
    me = api.verify_credentials()
    print("Giriş başarılı:", me.screen_name)
    tweet = "Bu bir test tweetidir. #test"
    api.update_status(tweet)
    print("Tweet atıldı.")
except Exception as e:
    print("Hata oluştu:", e)
