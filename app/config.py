import os
import dataclasses
from dotenv import load_dotenv

load_dotenv()

@dataclasses.dataclass(frozen=True)
class Settings:
    BOT_TOKEN: str = os.environ.get("BOT_TOKEN", "")
    CHAT_ID: str = os.environ.get("CHAT_ID", "")
    POSTGRES_USER: str = os.environ.get("POSTGRES_USER", "")
    POSTGRES_PASSWORD: str = os.environ.get("POSTGRES_PASSWORD", "")
    POSTGRES_HOST: str = os.environ.get("POSTGRES_HOST", "localhost")
    POSTGRES_PORT: str = os.environ.get("POSTGRES_PORT", "5432")
    POSTGRES_DB: str = os.environ.get("POSTGRES_DB", "")

    @property
    def db_url(self) -> str:
        return (
            f"postgresql://{self.POSTGRES_USER}:{self.POSTGRES_PASSWORD}"
            f"@{self.POSTGRES_HOST}:{self.POSTGRES_PORT}/{self.POSTGRES_DB}"
        )

settings = Settings()
