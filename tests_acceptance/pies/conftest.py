import pytest


@pytest.fixture
def get_testing_scenarios(request):
    if request.param == "scenario_1":
        return {"name": "John"}
    elif request.param == "scenario_2":
        return {"name": "Doe"}


@pytest.fixture
def get_number():
    return 111


@pytest.fixture
def get_magic_method2(get_number):
    def _wrapper(additional_number):
        return additional_number + get_number

    return _wrapper


def _magic_method():
    """
    например, удаление пользователя
    """
    return 17


@pytest.fixture
def get_magic_method(request):
    return _magic_method
