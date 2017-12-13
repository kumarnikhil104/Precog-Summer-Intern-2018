
try:
	from pymongo import MongoClient
	client = pymongo.MongoClient()
	db = client.precog
	coll = db.mumbai_tweets
	toAdd = db.fav_count

	fav_count = {100:0,90:0,
					80:0,70:0,
					60:0,50:0,
					40:0,30:0,
					20:0,10:0,0:0} 
	for tweet in coll.find():
	    md = tweet["Fav"]
	    for i in fav_count:
	        if md >= i:
	            fav_count[i] += 1
	            break

	print(fav_count)
	for x in fav_count:
	    jsonx = {"favs": x, "count": fav_count[x]}
	    toAdd.insert_one(jsonx)

except ImportError as e:
	print('ImportError'+str('e'))