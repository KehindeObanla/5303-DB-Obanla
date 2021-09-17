#main.py
import json
from mysqlCnx import MysqlCnx
from typing import Optional
from fastapi import FastAPI
from pydantic import BaseModel;

with open('/var/www/html/Database/.config.json') as f:
    config = json.loads(f.read())

cnx = MysqlCnx(**config)

app = FastAPI()

@app.get("/")
async def root():
    return {"message":"hello world"}

@app.get("/basics") 
async def getallbasic():
    result = cnx.query(f"SELECT * FROM sqlzoo WHERE groupname ='basics'") 
    finalresult =[]
    dictoparse = result['data']
    for item in result['data']:
        sql = item['query']
        quest = item['Question']
        answer = cnx.query(sql)
        response ={
            'result':answer['data'],
            'question':quest,
            'sql':sql
        }
        finalresult.append(response)
    return finalresult
@app.get("/basics/{count}")
async def getonebasic(count:int):
    result = cnx.query(f"SELECT * FROM sqlzoo WHERE groupname ='basics' AND count ={count}")
    if  len(result['data']) == 0 :
        return result
    else:
        sql = result['data'][0]['query']
        quest = result['data'][0]['Question']
        answer = cnx.query(sql)
        response ={
            'result':answer['data'],
            'question':quest,
            'sql':sql
        }
        return response
@app.get("/world")
async def getworldall():
    result = cnx.query(f"SELECT * FROM sqlzoo WHERE groupname ='world'") 
    finalresult =[]
    dictoparse = result['data']
    for item in result['data']:
        sql = item['query']
        quest = item['Question']
        answer = cnx.query(sql)
        response ={
            'result':answer['data'],
            'question':quest,
            'sql':sql
        }
        finalresult.append(response)
    return finalresult
@app.get("/world/{count}")
async def getonworld(count:int):
    result = cnx.query(f"SELECT * FROM sqlzoo WHERE groupname ='world' AND count ={count}")
    if  len(result['data']) == 0 :
        return result
    else:
        sql = result['data'][0]['query']
        quest = result['data'][0]['Question']
        answer = cnx.query(sql)
        response ={
            'result':answer['data'],
            'question':quest,
            'sql':sql
        }
        return response
@app.get("/nobel")
async def getnobelall():
    result = cnx.query(f"SELECT * FROM sqlzoo WHERE groupname ='nobel'") 
    finalresult =[]
    dictoparse = result['data']
    for item in result['data']:
        sql = item['query']
        quest = item['Question']
        answer = cnx.query(sql)
        response ={
            'result':answer['data'],
            'question':quest,
            'sql':sql
        }
        finalresult.append(response)
    return finalresult
@app.get("/nobel/{count}")
async def getnobelone(count:int):
    result = cnx.query(f"SELECT * FROM sqlzoo WHERE groupname ='nobel' AND count ={count}")
    if  len(result['data']) == 0 :
        return result
    else:
        sql = result['data'][0]['query']
        quest = result['data'][0]['Question']
        answer = cnx.query(sql)
        response ={
            'result':answer['data'],
            'question':quest,
            'sql':sql
        }
        return response
@app.get("/within")
async def getwithinall():
    result = cnx.query(f"SELECT * FROM `sqlzoo` WHERE groupname LIKE 'SELECT%'") 
    finalresult =[]
    dictoparse = result['data']
    for item in result['data']:
        sql = item['query']
        quest = item['Question']
        answer = cnx.query(sql)
        response ={
            'result':answer['data'],
            'question':quest,
            'sql':sql
        }
        finalresult.append(response)
    return finalresult
@app.get("/within/{count}")
async def getwithinone(count:int):
    result = cnx.query(f"SELECT * FROM sqlzoo WHERE groupname LIKE 'SELECT%' AND count ={count}")
    if  len(result['data']) == 0 :
        return result
    else:
        sql = result['data'][0]['query']
        quest = result['data'][0]['Question']
        answer = cnx.query(sql)
        response ={
            'result':answer['data'],
            'question':quest,
            'sql':sql
        }
        return response

@app.get("/aggregate")
async def getaggregateall():
    result = cnx.query(f"SELECT * FROM `sqlzoo` WHERE groupname ='SUMndCOUNT'") 
    finalresult =[]
    dictoparse = result['data']
    for item in result['data']:
        sql = item['query']
        quest = item['Question']
        answer = cnx.query(sql)
        response ={
            'result':answer['data'],
            'question':quest,
            'sql':sql
        }
        finalresult.append(response)
    return finalresult
@app.get("/aggregate/{count}")
async def getaggregateone(count:int):
    result = cnx.query(f"SELECT * FROM `sqlzoo` WHERE groupname ='SUMndCOUNT' AND count ={count}")
    if  len(result['data']) == 0 :
        return result
    else:
        sql = result['data'][0]['query']
        quest = result['data'][0]['Question']
        answer = cnx.query(sql)
        response ={
            'result':answer['data'],
            'question':quest,
            'sql':sql
        }
        return response
@app.get("/joins")
async def getjoinsall():
    result = cnx.query(f"SELECT * FROM `sqlzoo` WHERE groupname ='JOIN'") 
    finalresult =[]
    dictoparse = result['data']
    for item in result['data']:
        sql = item['query']
        quest = item['Question']
        answer = cnx.query(sql)
        response ={
            'result':answer['data'],
            'question':quest,
            'sql':sql
        }
        finalresult.append(response)
    return finalresult
@app.get("/joins/{count}")
async def getjoinsone(count:int):
    result = cnx.query(f"SELECT * FROM `sqlzoo` WHERE groupname ='JOIN' AND count ={count}")
    if  len(result['data']) == 0 :
        return result
    else:
        sql = result['data'][0]['query']
        quest = result['data'][0]['Question']
        answer = cnx.query(sql)
        response ={
            'result':answer['data'],
            'question':quest,
            'sql':sql
        }
        return response
    




    