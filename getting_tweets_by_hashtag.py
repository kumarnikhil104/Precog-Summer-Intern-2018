try:
	from credentials import consumer_key,consumer_secret
	from auth import get_twitter_client
	from tweepy import Cursor, AppAuthHandler, API
	from pymongo import MongoClient

	import tweepy
	import pymongo
	import jsonpickle
	import json
	import pprint

except ImportError:

	print("Some Error Occured in Importing the Modules and Library")


if __name__ =='__main__':
	auth=get_twitter_client()


'''
NOTE:	user-authentication	: 180 queries per access token every 15 minutes
	application- authentication : 450 queries every 15 minutes

Here we would be using application- authentication for higher rate limits.
For that we would have to use Tweepy's AppAuthHandler, we would need consumer_key and consumer_secret for that only

'''
auth =AppAuthHandler(consumer_key,consumer_secret)
api =API(auth,wait_on_rate_limit=True, wait_on_rate_limit_notify=True)
'''
NOTE: 
		1.The search API returns a maximum of 100 TWEETS per Query.
		2.We'll have to wait once our wait limit is reached.
		3.If not sure about the limits and want to check the status of your Rate Limit we can use the Tweepy's following method:
				print( api.rate_limit_status()['resource']['search'] )
'''
# pprint.pprint(api.rate_limit_status())  # IF YOU WANT TO LOOK ALL THE ATTRIBUTES
print(api.rate_limit_status()['resources']['search'] )

'''
We are all set for making the query we'll seprate the mutiple HASHTAGS by using OR.
Note: Try to keep the query less than 140 characters
'''
query_delhi='#myrighttobreathe OR #smog OR #crop Burning OR\
		 #delhi OR #delhichokes OR #AirPollution OR \
			#StopPollutionCrimes OR #letdelhibreathe OR #smoginDelhi OR \
			 #Delhi_Pollution OR #delhismog OR #delhipollution'

#query_mumbai='#CycloneOckhi OR #MumbaiRains OR #MumbaiRain OR #Cyclone OR #Ockhi'

max_no_of_tweets= 10000 		# The number of tweets you want to collect.
no_of_tweets_per_query=100 		# As Specified in the Note above
no_of_tweets_collected=0		# keeping count of the no. of tweets which has been collected
max_id= -1		# To remove redundancy

# MongoDB Connection

client_mongo=MongoClient('localhost',27017)		#By default it wait for connecitions on Port 27017
database=client_mongo['precog']
collection=database['delhi_tweets']		#Make another collection for mumbai_tweets when using query_mumbai

#-----------------------------------------------------------------------------------------------------------------------

with open('mummai_rain_cyclone.json','w') as f:

# While we want to keep collecting up to maximum no. of tweets
	while no_of_tweets_collected < max_no_of_tweets:
		try:
			if(max_id < 0):
				tweets = api.search(q=query_delhi, count=no_of_tweets_per_query,tweet_mode="extended")

			else:
				tweets = api.search(q=query_delhi,count=no_of_tweets_per_query,max_id=str(max_id-1),tweet_mode="extended")

			if not tweets:
				print("No More Tweets Found.")
				break

			for tweet in tweets:
				id=tweet.id_str
				user=tweet.user.name
				try:
					x =tweet.retweeted_status
					re_tweet=True

				except AttributeError:
					re_tweet=False

				if re_tweet:
					content=tweet.retweeted_status.full_text
					fav= -1 #Favorite count if Original Tweet

				else:
					content=tweet.full_text
					fav= tweet.favorite_count

				timestamp=str(tweet.created_at)
				location=tweet.user.location
				#h_tag is for hashtag
				h_tag = tweet.entities["hashtags"]
				hashtags=[]

				for i in h_tag:
					hashtags.append(i["text"])
					# this will create a list of hashtags in a tweet


				try:
					media_files= tweet.entities["media"]
					media=[]
					for i in media_files:
						media.append( i["url"] )
						#list of all the media files
				except KeyError:
					media =[]


				try:
					jsonx = {"_id":id,
								"user":user,
								"content":content,
								"timestamp":timestamp,
								"location":location,
								"hashtags":hashtags,
								"media":media,
								"Retweet":re_tweet,
								"Fav":fav
							}
				# we will store this json in our collection for further analysis
					collection.insert_one(jsonx)

				except pymongo.errors.DuplicateKeyError as e:
					print('Duplicate Data, Record Already Exist.')

			no_of_tweets_collected+=len(tweets)

			print("{0} tweets Downloaded".format(no_of_tweets_collected))
	# Record the id of the last tweet we looked at
			max_id=tweets[-1].id

		except tweepy.TweepError as e:
			#print the error and continue searching
			print("Error : "+str(e))

	print(" {0} tweets downloaded".format(no_of_tweets_collected))