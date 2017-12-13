try:
	import json
	import urllib
	import pymongo
	import requests

	# This is our google places API key
	KEY='AIzaSyB51gR5B-7G00MdIXC5AI4xRlpFvIRindk'

	client=pymongo.MongoClient()
	db=client.precog
	collection=db.delhi_tweets

	coll_loc=db.tweet_location

except ImportError as e:
	print('ImportError : '+str('e'))


def tweet_location(search_text):
	try:
		url='https://maps.googleapis.com/maps/api/place/textsearch/json'
		key='?key='+KEY
		query= '&query='+urllib.parse.quote(search_text)
		url = url+key+query
		response=json.loads(requests.get(url).text)
		addr = response['results'][0]['formatted_address']
		city = addr.split(",")[0]
		country=addr.split(",")[2]

		if country !='India':
			raise IndexError

	except IndexError:
		city='India'

	return city

i=0
location_count={}
for tweet in collection.find():
	i+=1
	location=tweet_location(tweet['location'])

	if loc not in location_count:
		location_count[loc]=1
	else:
		location_count[loc]+=1
	if i%10 == 0:
		print(str(i)+' of 10000 tweets')

for loc in location_count:
	jsonx={"city":loc,"tweets":str(location_count[loc])}
	coll_loc.insert_one(jsonx) # Document complete