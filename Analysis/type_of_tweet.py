
import pymongo
try:
	from pymongo import MongoClient
	client = pymongo.MongoClient()
	db = client.precog
	coll = db.mumbai_tweets

	#coll =db.delhi_tweets
	
	toAdd = db.type_count_mumbai

	type_count = {"text": 0, "image":0, "both":0} 
	for tweet in coll.find():
	    md = tweet["media"]
	    if len(md) != 0:
	        if tweet["content"] == "":
	            type_count["image"] += 1 
	        else:
	            type_count["both"] += 1
	    else:
	        type_count["text"] += 1

	jsonx = {"category": "text", "hits": str(type_count["text"])}
	print(jsonx)
	toAdd.insert_one(jsonx)
	jsonx = {"category": "image", "hits": str(type_count["image"])}
	print(jsonx)
	toAdd.insert_one(jsonx)
	jsonx = {"category": "both", "hits": str(type_count["both"])}
	print(jsonx)
	toAdd.insert_one(jsonx) # Sent to collections.

except ImportError as e:
	print('There is some ImportError.')