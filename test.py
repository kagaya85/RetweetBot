import tweepy
import random
import time
import KeysAndTokens as kt
from qqbot import qqbotsched

screen_name = 'KanColle_STAFF'
auth = tweepy.OAuthHandler(kt.consumer_key, kt.consumer_secret)
auth.set_access_token(kt.access_token, kt.access_token_secret)
api = tweepy.API(auth, proxy='127.0.0.1:1080')
alltweets = []
oldest_id = 0

new_tweets = api.user_timeline(screen_name, count = 5, tweet_mode="extended")
alltweets.extend(new_tweets)
oldest_id = alltweets[0].id

new_tweets = api.user_timeline(screen_name, count = 5, tweet_mode="extended", since_id = oldest_id)
alltweets.extend(new_tweets)
oldest_id = new_tweets[0].id
if len(new_tweets) > 0: 
    for tweet in new_tweets:
        print(tweet.created_at)