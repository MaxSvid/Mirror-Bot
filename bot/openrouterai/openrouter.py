import os
from dotenv import load_dotenv
load_dotenv()
import json
import requests

from config import settings

def test_token():
    print("Token Test")
    token = settings.OPENROUTER_API_KEY

    if not token:
        print("Error")
    else:
        print(f"Token: {token}")
    
if __name__ == "__main__":
    test_token() 