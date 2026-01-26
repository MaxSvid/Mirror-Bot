import os
from dotenv import load_dotenv
import dataclasses
from typing import Optional

load_dotenv()

@dataclasses.dataclass(frozen=True)
class GeminiConfig:
    """Configuration for Gemini AI API."""
    api_key: str = os.environ.get("GEMINI_API_KEY", "")
    model: str = "gemini-flash-latest"

@dataclasses.dataclass(frozen=True)
class Settings:
    """Global application settings."""
    # Bot settings
    BOT_TOKEN: str = os.environ.get("BOT_TOKEN", "")
    CHAT_ID: str = os.environ.get("CHAT_ID", "")
    COINGECKO_API: str = os.environ.get("COINGECKO_API", "")
    
    # API configurations
    gemini: GeminiConfig = dataclasses.field(default_factory=GeminiConfig)
    
    # Legacy support for GEMINI_API_KEY
    @property
    def GEMINI_API_KEY(self) -> str:
        return self.gemini.api_key

settings = Settings() 