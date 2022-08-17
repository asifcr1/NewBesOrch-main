import redis
import random
import time
import pickle
import json
from random import randrange

x = random.sample(range(10000), 10000)


def redisUsage():
    kk = 123
    r = redis.Redis(host='redis-16395.c78.eu-west-1-2.ec2.cloud.redislabs.com', port=16395, password="7B8TRG2SbyenKFc5O7j97cnpbZGPKvil")
    r.sadd('a', *x)
    members = r.smembers('a')
    return kk in members

def fileUsage():
    kk = 123
    with open("list", 'wb') as f:
        pickle.dump(x, f)
    with open("list", 'rb') as f:
        my_list = pickle.load(f)
    return kk in my_list




# start_time = time.time()
# redisUsage()
# print("--- %s seconds ---" % (time.time() - start_time))
#
# start_time = time.time()
# fileUsage()
# print("--- %s seconds ---" % (time.time() - start_time))

def function(n):

   values = ['value1', 'value2']
   mydict = {"key " + str(i): values[0] for i in range(n)}
   mydict["key " + str(random.randrange(n))] = values[1]

   return mydict


xx = function(100000)
print(type(xx))

def redisUsage():
    kk = 'key 98'
    r = redis.Redis(host='redis-16395.c78.eu-west-1-2.ec2.cloud.redislabs.com', port=16395, password="7B8TRG2SbyenKFc5O7j97cnpbZGPKvil" , encoding="utf-8", decode_responses="utf-8")
    r.hset('ad', mapping=xx)
    res = r.hget('ad',kk)
    return res

def fileUsage():
    kk = 'key 98'
    with open("dic", 'wb') as f:
        pickle.dump(xx, f)
    with open("dic", 'rb') as f:
        my_list = pickle.load(f)
    return my_list[kk]


start_time = time.time()
redisUsage()
print("--- %s seconds ---" % (time.time() - start_time))

start_time = time.time()
fileUsage()
print("--- %s seconds ---" % (time.time() - start_time))


