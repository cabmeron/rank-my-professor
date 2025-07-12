import requests
from pprint import pprint
from dataclasses import dataclass

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
