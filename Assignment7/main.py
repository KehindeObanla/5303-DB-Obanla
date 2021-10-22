#main.py
import uvicorn
import json
from mysqlCnx import MysqlCnx
from typing import Optional
from fastapi import FastAPI,Request
from pydantic import BaseModel;
from fastapi.responses import RedirectResponse,HTMLResponse



app = FastAPI()