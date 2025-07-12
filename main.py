import json
from functools import cache
from fastapi import FastAPI, HTTPException
from data_loader import load_school_json_file

app = FastAPI()

@app.get('/')
def root():
    return "Hello World"

@app.get('/schools/{school_name}/{department}')
def get_school_departments(school_name: str, department: str):

    data: dict = load_school_json_file(school_name)

    if(data is not None):
        with open('COE.json', 'w') as f:
            json.dump(data['University of Nevada, Reno']['College of Engineering'], f)
        return data['University of Nevada, Reno']['College of Engineering']

    return HTTPException(status_code=500, detail="Failed to Load School Data")