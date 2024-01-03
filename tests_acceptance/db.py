from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker, create_async_engine

from tests_acceptance.configuration import DB_PATH


Model = declarative_base(name="Model")

print(DB_PATH)
# engine = create_engine(f"sqlite+aiosqlite:///{DB_PATH}")
engine = create_async_engine(f"sqlite+aiosqlite:///{DB_PATH}")

# Session = sessionmaker(bind=engine, autoflush=False, autocommit=False)
Session = async_sessionmaker(bind=engine, autoflush=False, autocommit=False)

# session = Session()
