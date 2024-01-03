from pathlib import Path


SERVICE_URL = "http://localhost:8000"

BASE_DIR = Path(__file__).parent.parent

DB_PATH = BASE_DIR / "db.sqlite3"
