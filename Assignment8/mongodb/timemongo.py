import glob
import json
import time
import pymongo
import pprint
import random
import datetime
# connect to mongodb
with open('/var/www/html/Database/mongoconfig.json') as f:
    config = json.loads(f.read())
cnx = pymongo.MongoClient(**config)
#insert
start_time = time.time()
""" inserts =[5000,10000,50000,100000] """
mydb = cnx["testdata"]
mycol = mydb["customers"]
""" count = len(inserts)
alllist =[]
timeeach={} """
""" with  open("/var/www/html/Database/Assignment8/All.json", "r") as file1:
    data = json.load(file1)
    c =0
    while(count >0):
        count-=1
        currlist =[]
        i =0
        for i in range(i,inserts[c]):
            currlist.append(data[i])
        start_time = time.time()
        mycol.insert_many(currlist)
        endtime =(time.time() - start_time)
        keyfor = str(inserts[c])
        timeeach[keyfor] = endtime
        mycol.drop()
        print(inserts[c])
        c+=1
        print(count)
        print(timeeach)
alllist.append(timeeach)

with  open("/var/www/html/Database/Assignment8/timeall.json", "a") as file1:
    file1.write(json.dumps(alllist)) """

# bulk insert(100000)
""" with  open("/var/www/html/Database/Assignment8/All.json", "r") as file1:
    data = json.load(file1)
    c =3
    count-=1
    currlist =[]
    i =0
    for i in range(i,inserts[c]):
        currlist.append(data[i])
        count+=1
    mycol.insert_many(currlist)
    print(count) """
    

#search multiple
""" myquery ={'gender':Male,'Car'} """
""" start_time = time.time()

searchdic ={}
searchans =[]

result_5 = mycol.find({
    "$and" : [{
                 "gender" : "Male"
              },
              {
                   "Car" : "Elantra"
              }]
})
endtime =(time.time() - start_time)
searchdic['SearchMultiple'] = endtime
searchans.append(searchdic)
with  open("/var/www/html/Database/Assignment8/timeall.json", "a") as file1:
    file1.write(json.dumps(searchans)) """
#searchsingle
""" searchdic ={}
searchans =[]
start_time = time.time()
result_5 = mycol.find_one()
endtime =(time.time() - start_time)
searchdic['SearchSingle'] = endtime
searchans.append(searchdic)
with  open("/var/www/html/Database/Assignment8/timeall.json", "a") as file1:
    file1.write(json.dumps(searchans)) """
#update
update =[5000,10000,50000,100000]
inserts =[5000,10000,50000,100000]
mydb = cnx["testdata"]
mycol = mydb["customers"]
count = len(inserts)
alllist =[]
timeeach={}
updagegender ={'gender':"Female"} 
newvalues = { "$set": { "gender": "Male" } }
with  open("/var/www/html/Database/Assignment8/All.json", "r") as file1:
    data = json.load(file1)
    c =0
    while(count >0):
        count-=1
        currlist =[]
        i =0
        for i in range(i,inserts[c]):
            data[i]['gender']= "Female"
            currlist.append(data[i])
        mycol.insert_many(currlist)
        keyforupdate = str(inserts[c]) + "update"
        start_timeUpdate = time.time()
        mycol.update_many(updagegender, newvalues)
        endtimeupdate =(time.time() - start_timeUpdate)
        timeeach[keyforupdate] = endtimeupdate
        keyfordel = str(inserts[c]) + "delete"
        start_timedelete = time.time()
        mycol.delete_many({})
        endtimedelete =(time.time() - start_timedelete)
        timeeach[keyfordel] = endtimedelete
        mycol.drop()
        print(inserts[c])
        c+=1
        print(count)
        print(timeeach)
alllist.append(timeeach)

with  open("/var/www/html/Database/Assignment8/timeall.json", "a") as file1:
    file1.write(json.dumps(alllist))