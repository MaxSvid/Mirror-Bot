import os
from dotenv import load_dotenv

load_dotenv()

class Settings:
    BOT_TOKEN: str = os.environ.get("BOT_TOKEN") 
    GEMINI_API_KEY: str = os.environ.get("GEMINI_API_KEY")
    
settings = Settings() 