import os
from dotenv import load_dotenv

def get_api_key() -> str:
        load_dotenv()
        try:
            WEB_SCRAPER_API_KEY = os.getenv('SCRAPING_DOG_API_KEY')
        except:
            raise FileNotFoundError
        
        return WEB_SCRAPER_API_KEY
