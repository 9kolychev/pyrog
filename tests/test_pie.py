import pytest
import requests

from jsonschema import validate
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker, create_async_engine


from tests.configuration import SERVICE_URL
from tests.src.schemas.pie_jsonschema import PIE_SCHEMA
from tests.src.enums import GlobalErrorMessages as ErrMessage

from tests.src.base_classes import Response
from tests.src.schemas.pie import Pie


def test_get_pies():
    response = requests.get(url=f"{SERVICE_URL}/api/v1/pies")
    # print(response.__getstate__())
    received_posts = response.json()

    assert response.status_code == 200, ErrMessage.WRONG_STATUS_CODE.value
    for pie in received_posts:
        assert len(pie) == 5, ErrMessage.WRONG_ELEMENT_COUNT.value
        validate(pie, PIE_SCHEMA)

    # Response.validate(received_posts, POST_SCHEMA)
    # test_object.assert_status_code(300)


# def test_get_pie():
def test_get_pie(get_user_token, calculate):
    """
    Test get pie
    """
    print(get_user_token.get("access_token"))
    print(get_user_token.get("token_type"))

    print(calculate)
    print(calculate(2, 3))

    r = requests.get(url=f"{SERVICE_URL}/api/v1/pies/1")
    response = Response(r)

    response.assert_status_code(200)
    response.validate(Pie)


@pytest.mark.skip("Skip test")
def test_skip_test():
    assert 1 == 1


@pytest.mark.development
@pytest.mark.parametrize("a, b", [(1, 2), (-1, 2)], ids=str)
def test_parametrize_test(a, b, calculate):
    print(calculate(a, b))


@pytest.mark.parametrize("get_testing_scenarios", ["scenario_2"], indirect=True)
def test_scenarios(get_testing_scenarios):
    print(get_testing_scenarios)


def test_scenarios2(get_magic_method2):
    print(get_magic_method2(1))
    print(get_magic_method2(1))
    print(get_magic_method2(1))
    print(get_magic_method2(1))


# async def _load_all(session: AsyncSession):
#     q = select(Pies, id=1)
#     result = await session.execute(q)
#     curr = result.scalar()
#     # curr = result.scalars()
#     # for pie in curr:
#     #     print(pie)
#     return curr
#
#
# async def test_get_async_pie(get_pie):
#     session = get_pie
#     await _load_all(session=session)
