#main.py
import uvicorn
import json
from mysqlCnx import MysqlCnx
from typing import Optional
from fastapi import FastAPI,Request
from pydantic import BaseModel;
from fastapi.responses import RedirectResponse,HTMLResponse
from datetime import datetime



#helper function
def Timetwelve(converted):
    in_time = datetime.strptime(converted, "%H:%M:%S")
    out_time = datetime.strftime(in_time, "%I:%M:%p" )
    return out_time

def Timetwenty(converted):
    in_time = datetime.strptime(converted, "%I:%M%p")
    out_time = datetime.strftime(in_time, "%H:%M")
    return out_time

class Time(BaseModel):
    Begin:str
    End: Optional[str] = None


class filter(BaseModel):
        Col:  Optional[str] = None
        Crn: Optional[str] = None
        Subj: Optional[str] = None
        Crse: Optional[str] = None
        Sect:  Optional[str] = None
        Title: Optional[str] = None
        PrimaryInstructor:  Optional[str] = None
        Max: Optional[int] = None
        Curr: Optional[int] = None
        Aval:  Optional[int] = None
        Days:  Optional[str] = None
        Begin: Optional[str] = None
        End: Optional[str] = None
        Bldg:  Optional[str] = None
        Room: Optional[str] = None


""" Api """

app = FastAPI()

with open('/var/www/html/Database/.config.json') as f:
    config = json.loads(f.read())

cnx = MysqlCnx(**config)


@app.get("/courses/Crn/{Crn}")
async def CRN(Crn:str):
    sql = f'SELECT * FROM `CourseInfo` WHERE `Crn` ="{Crn}"'
    res = cnx.query(sql)
    result = res['data']
    result[0]['Begin'] =Timetwelve(str(result[0]['Begin']))
    result[0]['End']=Timetwelve(str(result[0]['End']))
    return result
@app.get("/courses/Subj/{Subj}")
async def Subj(Subj :str):
    sql = f'SELECT * FROM `CourseInfo` WHERE `Subj` ="{Subj}" ORDER BY `CourseInfo`.`year` DESC'
    res = cnx.query(sql)
    result = res['data']
    if(len(result) ==0):
        return 'invalid subject'
    else:

        response =[]
        for courses in result:
            if('Begin' in courses):
                courses['Begin'] = Timetwelve(str(courses['Begin']))
            if('End' in courses):
                courses['End'] = Timetwelve(str(courses['End']))
            response.append(courses)
        return response
@app.get("/courses/Crse/{Crse}")
async def Crse(Crse  :str):
    sql = f'SELECT * FROM `CourseInfo` WHERE `Crse` ="{Crse}" ORDER BY `CourseInfo`.`year` DESC'
    res = cnx.query(sql)
    result = res['data']
    if(len(result) ==0):
        return 'invalid course number'
    else:
        response =[]
        for courses in result:
            if('Begin' in courses):
                courses['Begin'] = Timetwelve(str(courses['Begin']))
            if('End' in courses):
                courses['End'] = Timetwelve(str(courses['End']))
            response.append(courses)
        return response
@app.get("/courses/Instructor/{name}")
async def Instructor(name :str):
    newname = name.lower() +'%'
    sql = f'SELECT * FROM `CourseInfo` WHERE `PrimaryInstructor` LIKE "{newname}" ORDER BY `CourseInfo`.`year` DESC'
    res = cnx.query(sql)
    result = res['data']
    if(len(result) ==0):
        return 'invalid name'
    else:
        response =[]
        for courses in result:
            if('Begin' in courses):
                courses['Begin'] = Timetwelve(str(courses['Begin']))
            if('End' in courses):
                courses['End'] = Timetwelve(str(courses['End']))
            response.append(courses)
        return response
@app.get("/courses/building/{Bldg}")
async def building(Bldg :str):
    sql = f'SELECT * FROM `CourseInfo` WHERE `Bldg`= "{Bldg}" ORDER BY `CourseInfo`.`year` DESC'
    res = cnx.query(sql)
    result = res['data']
    if(len(result) ==0):
        return 'invalid building'
    else:
        response =[]
        for courses in result:
            if('Begin' in courses):
                courses['Begin'] = Timetwelve(str(courses['Begin']))
            if('End' in courses):
                courses['End'] = Timetwelve(str(courses['End']))
            response.append(courses)
        return response


@app.get("/courses/Time/{Tyme}")
async def ClassTyme(Tyme:str):
    SplytTyme = Tyme.split(',')
    Begin = SplytTyme[0]
    if(len(SplytTyme) >1):
        End = SplytTyme[1]
    else:
        End =" "
    Begin = Timetwenty(str(Begin))
    if(End != " "):
        End = Timetwenty(str(End))
        sql =f'SELECT * FROM `CourseInfo` WHERE `Begin` >= "{Begin}" And `End` <= "{End}" ORDER BY `CourseInfo`.`year` DESC'
        res = cnx.query(sql)
        result = res['data']
        if(len(result) ==0):
            return 'invalid Time'
        else:
            response =[]
            for courses in result:
                if('Begin' in courses):
                    courses['Begin'] = Timetwelve(str(courses['Begin']))
                if('End' in courses):
                    courses['End'] = Timetwelve(str(courses['End']))
                response.append(courses)
            return response
@app.get("/courses/closed/")
async def Classclosed(): 
    sql =f'SELECT * FROM `CourseInfo` WHERE `Aval` = 0 ORDER BY `CourseInfo`.`year` DESC' 
    res = cnx.query(sql)
    result = res['data']
    if(len(result) ==0):
        return 'no available class'
    else:
        response =[]
        for courses in result:
            if('Begin' in courses):
                courses['Begin'] = Timetwelve(str(courses['Begin']))
            if('End' in courses):
                courses['End'] = Timetwelve(str(courses['End']))
            response.append(courses)
        return response  

@app.get("/courses/Title/{title}")
async def Instructor(title :str):
    newtitle = '%' + title.lower() +'%'
    sql = f'SELECT * FROM `CourseInfo` WHERE `Title` LIKE "{newtitle }" ORDER BY `CourseInfo`.`year` DESC'
    res = cnx.query(sql)
    result = res['data']
    if(len(result) ==0):
        return 'invalid Title'
    else:
        response =[]
        for courses in result:
            if('Begin' in courses):
                courses['Begin'] = Timetwelve(str(courses['Begin']))
            if('End' in courses):
                courses['End'] = Timetwelve(str(courses['End']))
            response.append(courses)
        return response

@app.post("/Annony")
async def filterall(sqlList:filter):
    print(sqlList.Col)
    sql ="SELECT * FROM `CourseInfo` WHERE year = 2022"
    response ={}
    if(sqlList.Col!=None):
        response['Col'] = sqlList.Col
    if(sqlList.Crn!=None):
        response['Crn'] = sqlList.Crn
    if(sqlList.Subj!=None):
        response['Subj'] = sqlList.Subj
    if(sqlList.Crse!=None):
        response['Crse'] = sqlList.Crse
    if(sqlList.Sect!=None):
        response['Sect'] = sqlList.Sect
    if(sqlList.Title!=None):
        response['Title'] = sqlList.Title
    if(sqlList.PrimaryInstructor!=None):
        response['PrimaryInstructor'] = sqlList.PrimaryInstructor
    if(sqlList.Max!=None):
        response['Max'] = sqlList.Max
    if(sqlList.Curr!=None):
        response['Curr'] = sqlList.Curr
    if(sqlList.Aval!=None):
        response['Aval'] = sqlList.Aval
    if(sqlList.Days!=None):
        response['Days'] = sqlList.Days
    if(sqlList.Begin!=None):
        response['Begin'] = sqlList.Begin
    if(sqlList.End!=None):
        response['End'] = sqlList.End
    if(sqlList.Bldg!=None):
        response['Bldg'] = sqlList.Bldg
    if(sqlList.Room!=None):
        response['Room'] = sqlList.Room
    sql = sql+" "
    for x,y in response.items():
        addand = 'AND'
        sql = sql + addand + " " + '`' + x +'`'  + " " + "="+ " "+ "'" +str(y) +"'"  
    sql = sql + ";"
    res = cnx.query(sql)
    result = res['data']
    if(len(result) ==0):
        return 'no available class'
    else:
        response =[]
        for courses in result:
            if('Begin' in courses):
                courses['Begin'] = Timetwelve(str(courses['Begin']))
            if('End' in courses):
                courses['End'] = Timetwelve(str(courses['End']))
            response.append(courses)
        return response