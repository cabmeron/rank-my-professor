import json
from functools import cache
from fastapi import HTTPException

@cache
def load_school_json_file(school_name):
    try:
        with open(f'{school_name}.json', 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        raise HTTPException(status_code=404, detail="School data file")
        
    
def get_school_departments_json(school_name):
     
    return load_school_json_file(school_name)