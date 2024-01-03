import pytest
import requests

from jsonschema import validate


from tests.configuration import SERVICE_URL
from tests.src.schemas.pie_jsonschema import PIE_SCHEMA
from tests.src.enums import GlobalErrorMessages as ErrMessage

from tests.src.base_classes import Response
from tests.src.schemas.pie import Pie, PieModel
from tests.helpers.data import pies


def test_get_pies(add_pies):
    """
    Test get all pies
    """
    r = requests.get(url=f"{SERVICE_URL}/api/v1/pies")
    # print(response.__getstate__())
    received_posts = r.json()

    assert r.status_code == 200, ErrMessage.WRONG_STATUS_CODE.value
    for pie in received_posts:
        assert len(pie) == 5, ErrMessage.WRONG_ELEMENT_COUNT.value
        validate(pie, PIE_SCHEMA)

    # Response.validate(received_posts, POST_SCHEMA)
    # test_object.assert_status_code(300)


def test_get_pie(add_pies):
    """
    Test get pie
    """
    pie_id, pie_model = add_pies
    r = requests.get(url=f"{SERVICE_URL}/api/v1/pies/{pie_id}")
    response = Response(r)

    response.assert_status_code(200)
    response.validate(Pie)
    response.assert_body(PieModel, pie_model)


@pytest.mark.skip
def test_calculate(calculate):
    print(calculate)
    print(calculate(2, 3))
