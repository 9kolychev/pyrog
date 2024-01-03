import json
import pytest
import requests

from tests.src.schemas.pie import Pie, PieModel
from tests.configuration import SERVICE_URL
from tests.helpers.data import pies

# from .src.generators.player import Player


def signin():
    userinfo = {
        "username": "testuser",
        "email": "testuser@example.com",
        "password": "mypass",
        "active": True,
    }
    r = requests.post(
        url=f"{SERVICE_URL}/api/v1/users/login",
        data=dict(
            username=userinfo.get("username"),
            password=userinfo.get("password"),
        ),
    )

    return r.json().get("access_token")


@pytest.fixture(scope="session")
def add_pies():
    apple_pie = PieModel(user_id=1, **pies.get("apple"))

    token = signin()

    r = requests.post(
        url=f"{SERVICE_URL}/api/v1/pies",
        headers={"Authorization": "Bearer {}".format(token)},
        data=apple_pie.model_dump_json(),
    )

    pie_id = r.json().get("id")

    if pie_id:
        yield pie_id, apple_pie
    else:
        raise TypeError("pie was not created")

    r = requests.delete(
        url=f"{SERVICE_URL}/api/v1/pies/{pie_id}",
        headers={"Authorization": "Bearer {}".format(token)},
        # params=dict(pie_id=pie_id),
    )


def _calculate(a: int | float, b: int | float) -> int | float:
    return a + b


@pytest.fixture()
def calculate():
    return _calculate


# if __name__ == "__main__":
#     a = {
#         "user_id": 1,
#         "name": "Apple Pie",
#         "description": "An apple pie is a fruit pie in which the principal filling is apples.",
#         "nutritional_value": "52% water, 34% carbohydrates, 2% protein, 11% fat.",
#         "id": 1,
#     }
#     b = {
#         "name": "Apple Pie",
#         "description": "An apple pie is a fruit pie in which the principal filling is apples.",
#         "nutritional_value": "52% water, 34% carbohydrates, 2% protein, 11% fat.",
#     }
#     # print(b.items() in a.items())
#
#     print(b.items() <= a.items())

# x = {"a": "Hello", "b": "World"}
# d = {"user_id": 1, **pies.get("apple")}
# print(d)
#
#
# @pytest.fixture()
# def generate_player():
#     return Player()
#
#
# # result = session.query(Pies).first()
#
# # if __name__ == "__main__":
# #     asyncio.run(main())
#
#
# def pytest_add_option(parser):
#     parser.addoption(
#         "--env",
#         default="development",
#         help="It is variable where our tests will be run. Possible values: prod, dev, qa",
#     )
#
#
# @pytest.fixture(autouse=True)
# def getting_env(request):
#     env = request.config.getoption("--env")
#     yield env
#
#
# import pytest
#
#
# @pytest.fixture
# def get_testing_scenarios(request):
#     if request.param == "scenario_1":
#         return {"name": "John"}
#     elif request.param == "scenario_2":
#         return {"name": "Doe"}
#
#
# @pytest.fixture
# def get_number():
#     return 111
#
#
# @pytest.fixture
# def get_magic_method2(get_number):
#     def _wrapper(additional_number):
#         return additional_number + get_number
#
#     return _wrapper
#
#
# def _magic_method():
#     """
#     например, удаление пользователя
#     """
#     return 17
#
#
# @pytest.fixture
# def get_magic_method(request):
#     return _magic_method
