
try:
	from pymongo import MongoClient
	client = pymongo.MongoClient()
	db = client.precog
	coll = db.mumbai_tweets
	toAdd = db.category_count_mumbai

	category_count = {"OT": 0, "RT":0}
	for tweet in coll.find():
	    m = tweet["Retweet"]
	    if m:
	        category_count["RT"] += 1 
	    else:
	        category_count["OT"] += 1 

	jsonx = {"category": "OT", "hits": str(category_count["OT"])}
	print(jsonx)
	toAdd.insert_one(jsonx)
	jsonx = {"category": "RT", "hits": str(category_count["RT"])}
	print(jsonx)
	toAdd.insert_one(jsonx)

except ImportError as e:
	print('There is some ImportError.')