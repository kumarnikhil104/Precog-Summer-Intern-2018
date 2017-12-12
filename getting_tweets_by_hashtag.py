try:
	from auth import get_twitter_client
	from tweepy import Cursor, AppAuthHandler, API
	from pymongo import MongoClient

	import jsonpickle
	import json

except ImportError:

	print("Some error in Importing the Modules and Library")


if __name__ =='__main__':
	auth=get_twitter_client()