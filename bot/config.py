import os
import dataclasses
from dotenv import load_dotenv

load_dotenv()

@dataclasses(frozen=True)
class Settings:
    BOT_TOKEN: str = os.getenv("BOT_TOKEN", "")

settings = Settings()