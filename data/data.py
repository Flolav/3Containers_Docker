import redis
import time

cache = redis.Redis(host='redis', port=6379,charset="utf-8",decode_responses=True)

def add_sentences_to_hash(txt1,txt2,similarity):
    dict = {"sentence1":txt1,
            "sentence2":txt2,
            "similarity":str(similarity)}
   
    key = "timestamp_"+str(int(time.time()))
    cache.hmset(key,mapping=dict)

def get_past_inputs():
    query_list = []
    keys = cache.keys("timestamp_*")

    for key in keys:
        query = cache.hgetall(key)
        query_list.append(query)
   
    return query_list