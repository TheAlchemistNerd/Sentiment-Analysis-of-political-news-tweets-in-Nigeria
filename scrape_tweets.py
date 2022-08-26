import os
import tweepy
import json
import requests
import pandas as pd
from dotenv import load_dotenv

# loads a '.env' file that contains the authentication keys
load_dotenv()

# authentication keys
consumer_key = os.environ["API_KEY"]
consumer_secret = os.environ["API_KEY_SECRET"]
bearer_token = os.environ["BEARER_TOKEN"]
access_token = os.environ["ACCESS_TOKEN"]
access_token_secret = os.environ["ACCESS_TOKEN_SECRET"]


client = tweepy.Client(bearer_token=bearer_token)

# client = tweepy.Client(bearer_token=bearer_token, return_type = requests.Response)

query =  'nigeria (political OR fake) news -is:retweet'

tweets = tweepy.Paginator(client.search_recent_tweets, query=query, tweet_fields=['context_annotations', 'created_at'], max_results=100)

tweets_data = []
for tweet in tweets.flatten(limit=1000):
    tweet_dict = {'id':tweet.id, 'text':tweet.text, 'date_created':tweet.created_at}
    tweets_data.append(tweet_dict)

# tweets = client.search_recent_tweets(
#    query=query,
#    tweet_fields=['context_annotations', 'created_at'], max_results=10,
#   )

#tweets_json = tweets.json()
#tweets_json
#tweets_data = tweets_json['data']


df = pd.json_normalize(tweets_data) 
df.to_csv('output_2.csv')

print("Scrapping successful")