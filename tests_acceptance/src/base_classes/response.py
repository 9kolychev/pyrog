import requests

from jsonschema import validate

from tests_acceptance.src.enums import GlobalErrorMessages as ErrMessage


class Response:
    def __init__(self, response: requests.models.Response):
        self.response = response
        self.response_json = response.json()
        # self.response_json = response.json().get("data")
        self.response_status = response.status_code
        self.parsed_object = {}

    def validate(self, schema):
        if isinstance(self.response_json, list):
            for item in self.response_json:
                schema.model_validate(item)
                # validate(item, schema)  # for jsonschema
        else:
            schema.model_validate(self.response_json)
            # validate(self.response_json, schema)
        return self

    def assert_status_code(self, status_code):
        if isinstance(status_code, list):
            assert (
                self.response_status
                in status_code
                # ), ErrMessage.WRONG_STATUS_CODE.value
            ), self
        else:
            assert self.response_status == status_code, self
            # ), ErrMessage.WRONG_STATUS_CODE.value
        return self

    def get_parsed_object(self, schema):
        if isinstance(self.response_json, list):
            for item in self.response_json:
                self.parsed_object = schema.parse_obj(item)
            else:
                self.parsed_object = schema.parse_obj(self.response_json)
        return self.parsed_object

    def __str__(self):
        return (
            f"\nStatus code: {self.response_status}"
            f"\nRequested url: {self.response.url}"
            f"\nResponse body: {self.response_json}"
        )
