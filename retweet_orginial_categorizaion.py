# Queries the all_tweets collection and creates a new collection with the distribution of categories.
import pymongo

client = pymongo.MongoClient()
db = client.precog
coll = db.mumbai_tweets
toAdd = db.category_count_mumbai

category_count = {"OT": 0, "RT":0}
for tweet in coll.find():
    md = tweet["Retweet"]
    if md:
        category_count["RT"] += 1 # Original Tweets
    else:
        category_count["OT"] += 1 # Re Tweets

jsonx = {"category": "OT", "hits": str(category_count["OT"])}
print(jsonx)
toAdd.insert_one(jsonx)
jsonx = {"category": "RT", "hits": str(category_count["RT"])}
print(jsonx)
toAdd.insert_one(jsonx)