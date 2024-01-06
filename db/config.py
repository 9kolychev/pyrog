from pathlib import Path
from pydantic import BaseModel
from pydantic_settings import BaseSettings


BASE_DIR = Path(__file__).parent.parent

DB_PATH = BASE_DIR / "db.sqlite3"

REAL_DATABASE_URL = "postgresql+asyncpg://postgres:postgres@0.0.0.0:5432/postgres"
TEST_DATABASE_URL = (
    "postgresql+asyncpg://postgres_test:postgres_test@0.0.0.0:5433/postgres_test"
)


class DBSettings(BaseModel):
    url: str = f"sqlite+aiosqlite:///{DB_PATH}"
    echo: bool = True
    # echo: bool = False


class AuthJWT(BaseModel):
    private_key_path: Path = BASE_DIR / "certs" / "jwt-private.pem"
    public_key_path: Path = BASE_DIR / "certs" / "jwt-public.pem"
    algorithm: str = "RS256"
    access_token_expire_minutes: int = 15


class Settings(BaseSettings):
    api_v1_prefix: str = "/api/v1"

    db: DBSettings = DBSettings()

    auth_jwt: AuthJWT = AuthJWT()


settings = Settings()
