import glob
import json
import time
import pymongo
import pprint
import random

# connect to mongodb
with open('/var/www/html/Database/mongoconfig.json') as f:
    config = json.loads(f.read())
cnx = pymongo.MongoClient(**config)
start_time = time.time()
inserts =[50000,100000,500000,1000000]
mydb = myclient["mydatabase"]
mycol = mydb["customers"]
timeeach=[]
with  open("/var/www/html/Database/Assignment8/All.json", "a") as file1:
    data = json.load(file1)
    c =0
    for i in range(i,inserts[c]):
