# Queries the all_tweets collection and creates a new collection with the distribution of the types of tweet based on content.
import pymongo

client = pymongo.MongoClient()
db = client.precog
coll = db.mumbai_tweets
#coll =db.delhi_tweets
toAdd = db.type_count

type_count = {"text": 0, "image":0, "both":0} 
for tweet in coll.find():
    md = tweet["media"]
    if len(md) != 0:
        if tweet["content"] == "":
            type_count["image"] += 1 # STILL LOOKING FOR SUCH A TWEET :/
        else:
            type_count["both"] += 1 # COMMON
    else:
        type_count["text"] += 1 # COMMON

jsonx = {"category": "text", "hits": str(type_count["text"])}
print(jsonx)
toAdd.insert_one(jsonx)
jsonx = {"category": "image", "hits": str(type_count["image"])}
print(jsonx)
toAdd.insert_one(jsonx)
jsonx = {"category": "both", "hits": str(type_count["both"])}
print(jsonx)
toAdd.insert_one(jsonx) # Sent to collections.