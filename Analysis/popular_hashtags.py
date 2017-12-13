
try:
    from pymongo import MongoClient
    client = pymongo.MongoClient()
    db = client.precog
    coll = db.delhi_tweets

    #coll=db.mumbai_tweets

    toAdd = db.hash_count_mumbai

    hashtag_count = {}
    for tweet in coll.find():
        ht = tweet["hashtags"]
        for hash in ht:
            hash = hash.lower()
            if hash not in hashtag_count: # Adding and checking dem hashtags.
                hashtag_count[hash] = 1
            else:
                hashtag_count[hash] += 1

    hc = sorted(hashtag_count, key=hashtag_count.get, reverse=True) # Sorting and slicing to get the top 10.
    count = 0

    for z in hc:
        if count == 15: # getting 13 popular tweets
            break
        jsonx = {"hashtag": z, "count": str(hashtag_count[z])}
        toAdd.insert_one(jsonx)
        count += 1