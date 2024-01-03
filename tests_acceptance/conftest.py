import pytest
import requests
from sqlalchemy import Boolean, Column, Integer, String, select
import asyncio
from tests_acceptance.db import Model, Session, AsyncSession


from tests_acceptance.configuration import SERVICE_URL
from tests_acceptance.tables import Pies
from .src.generators.player import Player


def pytest_configure():
    pass


@pytest.fixture()
def get_user_token():
    response = requests.post(
        url=f"{SERVICE_URL}/api/v1/users/login/",
        data={"username": "john", "password": "1Password!"},
    )
    # Create user
    yield response.json()
    # Delete user


def _calculate(a: int | float, b: int | float) -> int | float:
    return a + b


@pytest.fixture()
def calculate():
    return _calculate


@pytest.fixture()
def generate_player():
    return Player()


@pytest.fixture()
async def get_pie():
    async with Session() as session:
        yield session


# result = session.query(Pies).first()

# if __name__ == "__main__":
#     asyncio.run(main())


def pytest_add_option(parser):
    parser.addoption(
        "--env",
        default="development",
        help="It is variable where our tests will be run. Possible values: prod, dev, qa",
    )


@pytest.fixture(autouse=True)
def getting_env(request):
    env = request.config.getoption("--env")
    yield env
