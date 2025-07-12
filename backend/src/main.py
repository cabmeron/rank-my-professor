import json
from env import *
from scrape import *
from functools import cache
from fastapi import FastAPI, HTTPException
from data_loader import load_school_json_file

app = FastAPI()

@app.get('/')
def root():
    return "Hello World"

@app.get('/schools/unr/cse')

def get_unr_cse_employees():

    data = load_school_json_file('../data/colleges/unr/COE_scraped_formatted')

    profiles = []
    
    for profile in data['profiles']:
        for author in profile['authors']:
            profiles.append(
                (
                    author['cited_by'],
                    author['name'],
                    author['link']
                )
            )
    
    sorted_profiles = sorted(profiles, key=lambda tup: -tup[0])

    return sorted_profiles

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