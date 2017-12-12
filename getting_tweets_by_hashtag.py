try:
	from credentials import consumer_key,consumer_secret
	from auth import get_twitter_client
	from tweepy import Cursor, AppAuthHandler, API
	from pymongo import MongoClient

	import jsonpickle
	import json
	import pprint
except ImportError:

	print("Some Error Occured in Importing the Modules and Library")


if __name__ =='__main__':
	auth=get_twitter_client()


'''
NOTE:	user-authentication			: 180 queries per access token every 15 minutes
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

no_of_tweets= 10000 		# The number of tweets you want to collect.
no_of_tweets_per_query=100  	# As Specified in the Note above
collected_tweet=0 			# keeping count of the no. of tweets which has been collected

