from credentials import consumer_key, consumer_secret,access_token,access_token_secret
from tweepy.auth import OAuthHandler
from tweepy import API
import os
import sys

def get_twitter_auth():
	# pass the consumer key and secret to the Tweepy's user authentication handler
	auth= OAuthHandler(consumer_key,consumer_secret)
	# pass the access token and secret to Tweepy's user authentication handler
	auth.set_access_token(access_token,access_token_secret)

	return auth

	if KeyError:
		sys.stderr.write("Twitter Authentication Keys are Invalid.\n")
		sys.exit(1) # exits from the program 

def get_twitter_client():
	''' setting up the twitter API client
		return : tweepy.API object
	'''
# creating a twitter API wrapper using tweepy
	auth=get_twitter_auth()# calling the authorization function
	client=API(auth)
	print('---------Authentication Successfull---------')

	return client
	
if __name__ =='__main__':
	client=get_twitter_client()

