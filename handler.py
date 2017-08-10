from reply_generator import reply_generator


import insults
import random
import tweepy
import datetime

trump_id = '25073877'




def get_twitter_client(consumer_key, consumer_secret, access_token, access_secret):
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_secret)
    api = tweepy.API(auth)
    return api

    

def streaming_insulter():
    twitter = get_twitter_client()
    api.update_status(
        reply_generator(), 
        in_reply_to_status_id=tweetid
    )

def periodic_insulter():
    twitter = get_twitter_client()
    reply_generator()
Config.get('storage', 'last_tweet_sent').title(),

    listener = StdOutListener()
    twitterStream = Stream(auth, listener)
    twitterStream.filter(follow=trump_id)
