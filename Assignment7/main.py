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

def formatResult(res):
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

class AdvisingForms(BaseModel):
    StudentID:Optional[str] = None
    Semester:Optional[str] = None
    Year:Optional[str] = None



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
        return formatResult(res)
@app.get("/courses/Crse/{Crse}")
async def Crse(Crse  :str):
    sql = f'SELECT * FROM `CourseInfo` WHERE `Crse` ="{Crse}" ORDER BY `CourseInfo`.`year` DESC'
    res = cnx.query(sql)
    result = res['data']
    if(len(result) ==0):
        return 'invalid course number'
    else:
        return formatResult(res)
@app.get("/courses/Instructor/{name}")
async def Instructor(name :str):
    newname = name.lower() +'%'
    sql = f'SELECT * FROM `CourseInfo` WHERE `PrimaryInstructor` LIKE "{newname}" ORDER BY `CourseInfo`.`year` DESC'
    res = cnx.query(sql)
    result = res['data']
    if(len(result) ==0):
        return 'invalid name'
    else:
        return formatResult(res)
@app.get("/courses/building/{Bldg}")
async def building(Bldg :str):
    sql = f'SELECT * FROM `CourseInfo` WHERE `Bldg`= "{Bldg}" ORDER BY `CourseInfo`.`year` DESC'
    res = cnx.query(sql)
    result = res['data']
    if(len(result) ==0):
        return 'invalid building'
    else:
        return formatResult(res)


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
            return formatResult(res)
@app.get("/courses/closed/")
async def Classclosed(): 
    sql =f'SELECT * FROM `CourseInfo` WHERE `Aval` = 0 ORDER BY `CourseInfo`.`year` DESC' 
    res = cnx.query(sql)
    result = res['data']
    if(len(result) ==0):
        return 'no available class'
    else:
        return formatResult(res)  

@app.get("/courses/Title/{title}")
async def Instructor(title :str):
    newtitle = '%' + title.lower() +'%'
    sql = f'SELECT * FROM `CourseInfo` WHERE `Title` LIKE "{newtitle}" ORDER BY `CourseInfo`.`year` DESC'
    res = cnx.query(sql)
    result = res['data']
    if(len(result) ==0):
        return 'invalid Title'
    else:
        return formatResult(res)

@app.get("/courses/buildingndroom/{buldroom}")
async def ClassTyme(buldroom:str):
    SplytTyme = buldroom.split(',')
    Bldg = SplytTyme[0]
    if(len(SplytTyme) >1):
        Room = SplytTyme[1]
        newRoom = '%' + Room +'%'
    else:
        Room =" "
    if(Room != " "):
        sql =f'SELECT * FROM `CourseInfo` WHERE `Bldg` = "{Bldg}" And `Room` LIKE "{newRoom}" ORDER BY `CourseInfo`.`year` DESC'
        res = cnx.query(sql)
        result = res['data']
        if(len(result) ==0):
            return 'invalid room or building'
        else:
            return formatResult(res)

@app.post("/Annony")
async def filterall(sqlList:filter):
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
        return formatResult(res)

@app.get("/student")
async def Allstudent():
    sql ='SELECT * FROM `StudentIInfo`'
    res = cnx.query(sql)
    
    return formatResult(res)

@app.get("/student/Mnumber/{Mnumber}")
async def StudentMnumber (Mnumber:str):
    sql =f'SELECT * FROM `StudentIInfo` WHERE `Mnumber` ="{Mnumber}"'
    res = cnx.query(sql)
    result = res['data']
    if(len(result) ==0):
        return 'Invalid Mnumber'
    else:
        return formatResult(res)
@app.get("/student/Name/{Name}")
async def studentName (Name:str):
    splitname =Name.split(',')
    Fname = splitname[0]
    Lname = splitname[1]
    sql =f'SELECT * FROM `StudentIInfo` WHERE `FirstName`="{Fname}"and `LastName`="{Lname}"'
    res = cnx.query(sql)
    result = res['data']
    if(len(result) ==0):
        return 'Invalid name'
    else:
        return formatResult(res)

@app.get("/student/GPAG/{GPA}")
async def GPAG (GPA:int):
    sql =f'SELECT * FROM `StudentIInfo` WHERE `GPA` >= "{GPA}"'
    res = cnx.query(sql)
    result = res['data']
    if(len(result) ==0):
        return 'Invalid GPA'
    else:
        return formatResult(res)

@app.get("/student/GPAL/{GPA}")
async def GPAL(GPA:int):
    sql =f'SELECT * FROM `StudentIInfo` WHERE `GPA` <= "{GPA}"'
    res = cnx.query(sql)
    result = res['data']
    if(len(result) ==0):
        return 'Invalid GPA'
    else:
        return formatResult(res)

@app.get("/Advising")
async def Advising ():
    sql =f'SELECT * FROM `Advisingform`'
    res = cnx.query(sql)
    
    return formatResult(res)

@app.get("/Advising/student/{Mnumber}")
async def AdvisingStudentnum(Mnumber:str):
    sql =f'SELECT * FROM `Advisingform` WHERE `StudentID` ="{Mnumber}"'
    res = cnx.query(sql)
    result = res['data']
    if(len(result) ==0):
        return 'Invalid number'
    else:
        return formatResult(res)

@app.get("/Advising/Semester/{Semester}")
async def AdvisingStudentSemester (Semester:str):
    sql =f'SELECT * FROM `Advisingform` WHERE `Semester`="{Semester}"'
    res = cnx.query(sql)
    result = res['data']
    if(len(result) ==0):
        return 'Invalid Semester'
    else:
        return formatResult(res)
@app.get("/Advising/year/{year}")
async def AdvisingStudentyear (Semester:str):
    sql =f'SELECT * FROM `Advising form` WHERE `Year`="{year}"'
    res = cnx.query(sql)
    result = res['data']
    if(len(result) ==0):
        return 'Invalid Year'
    else:
        return formatResult(res)

@app.post("/Advising/All")
async def filterAdvisform(Advisform:AdvisingForms):
    count =0
    response ={}
    sql ="SELECT * FROM `Advisingform` WHERE"
    if(Advisform.StudentID!=None):
        response['StudentID'] = Advisform.StudentID
    if(Advisform.Semester!=None):
        response['Semester'] = Advisform.Semester
    if(Advisform.Year!=None):
        response['Year'] = Advisform.Year
    if(len(response)>1):
        for x,y in response.items():
            sql = sql + " " + '`' + x +'`'  + " " + "="+ " "+ "'" +str(y) +"'"  
            del response[x]
            break
        for x,y in response.items():
            addand = 'AND'
            sql = sql + addand + " " + '`' + x +'`'  + " " + "="+ " "+ "'" +str(y) +"'"      
    else:
        for x,y in response.items():
            sql = sql + " " + '`' + x +'`'  + " " + "="+ " "+ "'" +str(y) +"'"  
    sql = sql + ";"
    res = cnx.query(sql)
    result = res['data']
    if(len(result) ==0):
        return 'Invalid Advising filters'
    else:
        return formatResult(res)