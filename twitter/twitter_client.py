import os
import sys
from tweepy import API
from tweepy import OAuthHandler

'''
	Setup Twitter authentication.
	Return : tweepy.OAuthHandler object
'''

def get_twitter_auth():
	try:
		consumer_key = os.environ['TWITTER_CONSUMER_KEY']
		consumer_secret = os.environ['TWITTER_CONSUMER_SECRET']
		access_key = os.environ['TWITTER_ACCESS_KEY']
		access_secret = os.environ['TWITTER_ACCESS_SECRET']
	except KeyError:
		sys.stderr.write("TWITTER_* environmental variable not set\n")
		sys.exit(1)
	auth = OAuthHandler(consumer_key, consumer_secret)
	auth.set_access_token(access_key, access_secret)
	return auth

'''
	Setup Twitter API client
	Return : tweepy.API object
'''

def get_twitter_client():
	auth = get_twitter_auth()
	client = API(auth)
	return client
