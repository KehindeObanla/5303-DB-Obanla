import pymongo
import pprint
import random
import json



app = FastAPI()
# connect to mongodb
with open('/var/www/html/Database/mongoconfig.json') as f:
    config = json.loads(f.read())
cnx = pymongo.MongoClient(**config)