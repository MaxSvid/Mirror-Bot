import os
from dotenv import load_dotenv
load_dotenv()

from bot.config import settings

API_KEY = os.getenv("OPENROUTER_API_KEY")