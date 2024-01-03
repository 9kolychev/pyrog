from os import getenv
from pathlib import Path
from pydantic_settings import BaseSettings


BASE_DIR = Path(__file__).parent.parent

REAL_DATABASE_URL = "postgresql+asyncpg://postgres:postgres@0.0.0.0:5432/postgres"
TEST_DATABASE_URL = (
    "postgresql+asyncpg://postgres_test:postgres_test@0.0.0.0:5433/postgres_test"
)


class Settings(BaseSettings):
    api_v1_prefix: str = "/api/v1"

    db_url: str = f"sqlite+aiosqlite:///{BASE_DIR}/db.sqlite3"
    db_echo: bool = True
    # db_echo: bool = False


settings = Settings()
