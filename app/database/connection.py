import psycopg
from psycopg import AsyncConnection

from app.config import settings


async def get_connection() -> AsyncConnection:
    """Return an async PostgreSQL connection."""
    return await AsyncConnection.connect(settings.db_url)
