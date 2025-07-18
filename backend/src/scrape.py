import json
import requests
from pprint import pprint
from dataclasses import dataclass
from data_loader import load_school_json_file

@dataclass(frozen=True)
class parameterized_request:
     url: str
     query: str
     api_key: str
     language: str
     results: int
     page: int

def parameterize_request(query:str, api_key: str, language:str="en", page:int=0, results:int=10) -> parameterized_request:
    return parameterized_request(
        url="https://api.scrapingdog.com/google_scholar",
        query=query,
        api_key=api_key,
        language=language,
        results=results,
        page=page
    )

def query_google_scholar(preq: parameterized_request) -> dict:

    url = preq.url

    params = {
        "page": preq.page,
        "query": preq.query,
        "api_key": preq.api_key,
        "language": preq.language,
        "results": preq.results,
    }

    response = requests.get(url, params=params)
  
    if response.status_code == 200:
        data = response.json()
        pprint(data['profiles'])
        return data

    else:
        print(f"Request failed with status code: {response.status_code}")
        print(f"Response Body: {response.content}")

def compute_unr_cse_employees():

    data = load_school_json_file('../data/colleges/unr/COE_scraped_formatted')

    profiles = []
    
    for profile in data['profiles']:
        for author in profile['authors']:
            profiles.append(
                {
                    "cited_by": author['cited_by'],
                    "name": author['name'],
                    "gs_link": author['link']
                }
            )
    
    sorted_profiles = sorted(profiles, key=lambda tup: -tup['cited_by']) 

    with open('unr-cse.json', 'w') as f:
        json.dump(sorted_profiles, f, indent=5)