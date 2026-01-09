import os
import requests
from bs4 import BeautifulSoup

from dotenv import load_dotenv
load_dotenv() 

from job_config import website

try:
    response = requests.get(website.DJINNI_JOBS_URL)
    response.raise_for_status()
    print("Connection works = 200")
except requests.exceptions.RequestException as e:
    print(f"Request failed: {e}")

