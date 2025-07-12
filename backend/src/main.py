import json
from env import *
from scrape import *
from functools import cache
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from data_loader import load_school_json_file

origins = [ "http://127.0.0.1:5500" ]

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

@app.get('/')
def root():
    return "Hello World"

@app.get('/schools/{college}/{department}')
def get_college_employees(college: str, department: str):

    data = load_school_json_file(f'unr-{department}')
    return data

@app.get('/schools/unr/CoE')
def get_unr_cse():

    data = load_school_json_file('COE')
    # api_key = get_api_key()
    
    if(data is not None):
        
        # unr_cse = data['Department of Computer Science and Engineering']
        # json_list = []
    
        # with open('COE_scraped_data.json', 'a') as f:
        #     for employee in unr_cse:
        #         paramaterized_req = parameterize_request(
        #             query=employee['name'],
        #             api_key=api_key,
        #             results=1
        #         )

        #         res = query_google_scholar(paramaterized_req)
        #         json.dump(res, f)

        # json_data = json.load('COE_scraped_data.json')

        # pprint(json_data)
       
        return data
    
    return HTTPException(status_code=500, detail='Internal Server Processing Error')

@app.get('/schools/{school_name}/{department}')
def get_school_departments(school_name: str, department: str):

    data: dict = load_school_json_file(school_name)

    if(data is not None):
        with open('COE.json', 'w') as f:
            json.dump(data['University of Nevada, Reno']['College of Engineering'], f)
        return data['University of Nevada, Reno']['College of Engineering']

    return HTTPException(status_code=500, detail="Internal Server Processing Error")