import json
from env import *
from scrape import *
from functools import cache
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from data_loader import load_school_json_file

origins = [ "http://127.0.0.1:5500" ]

app = FastAPI()

app.add_middleware( CORSMiddleware, allow_origins=origins, allow_credentials=True, allow_methods=["*"], allow_headers=["*"] )

@app.get('/schools/{college}/{department}')
def get_college_employees(college: str, department: str):
    data = load_school_json_file(f'unr-{department}')
    return data
