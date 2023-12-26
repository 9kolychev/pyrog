import asyncio
from typing import Generator

from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker

import pytest
import os

import settings


test_engine = create_async_engine(
    settings.TEST_DATABASE_URL,
    future=True,
    echo=True,
)

async_session = sessionmaker(
    test_engine,
    expire_on_commit=False,
    class_=AsyncSession,
)


@pytest.fixture(scope="session")
def event_loop():
    loop = asyncio.get_event_loop_policy().new_event_loop()
    yield loop
    loop.close()


@pytest.fixture(scope="session")
def asyncpg_pool():
    pool = asyncpg.create_pool("".join(settings.TEST_DATABASE_URL.split("+asyncpg")))
    yield pool
    pool.close()


@pytest.fixture(autouse=True, scope="session")
async def prepare_database():
    async with test_engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    yield
    async with test_engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)
