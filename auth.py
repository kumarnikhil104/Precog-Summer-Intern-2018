from tweepy.auth import OAuthHandler
from tweepy import API
import os
import sys

def get_twitter_auth():
	''' return : tweepy.OAuthHandler Object'''
	try:
		consumer_key = 'yKzRSnv63u4nhWGkzYDtmdTe5'
		consumer_secret = 'qxPhFk7VPmtVaNTWhB20Pqeakb57V3uZbjhtfyjjAw1L5rQqVk'
		access_token = '3074692450-CyWz6HSf1XTZGRaV9bRswDLwKcmoGoWZTlXAOD1'
		access_token_secret = 'jiIU8pVrzeK0B8whx5YFJhvMwoHGHrWHZGbDI6SG9dJNf'

	except KeyError:
		sys.stderr.write("Twitter Authentication Keys are Invalid.\n")
		sys.exit(1) # exits from the program 

# pass the consumer key and secret to the Tweepy's user authentication handler
	auth= OAuthHandler(consumer_key,consumer_secret)
# pass the access token and secret to Tweepy's user authentication handler
	auth.set_access_token(access_token,access_token_secret)

	return auth

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

