import os
from dotenv import load_dotenv

import dataclasses

load_dotenv()

@dataclasses.dataclass(frozen=True)
class Settings:
    BOT_TOKEN: str = os.environ.get("BOT_TOKEN")
    CHAT_ID: str = os.environ.get("CHAT_ID")
    GEMINI_API_KEY: str = os.environ.get("GEMINI_API_KEY")

settings = Settings() 