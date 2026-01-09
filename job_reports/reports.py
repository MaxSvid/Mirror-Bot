import os
import requests
from bs4 import BeautifulSoup

from dotenv import load_dotenv
load_dotenv() 

from job_config import website

try:
    response = requests.get(website.DJINNI_JOBS_URL,
                            headers={"User-Agent": "Mozilla/5.0"})
    response.raise_for_status()
    print("Connection works = 200")
except requests.exceptions.RequestException as e:
    print(f"Request failed: {e}")


# Get HTML code page:
html_content = response.text
soup = BeautifulSoup(html_content, "html.parser")

# Сheck page title: 
title = soup.title.text
print(f"Page title: {title}")

# Finding all jobs offers:
jobs = soup.find_all("a", class_="job-item__title-link")[:15] # list that keeps only first 20 jobs for right now
print(f"Found: {len(jobs)}")

for job in jobs:
    url = "https://djinni.co" + job.get("href")
    print(url)
