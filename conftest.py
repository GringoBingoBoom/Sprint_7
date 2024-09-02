import pytest

import urls
from helpers import CreatePayload
from scooter_api import ApiRequestPost


@pytest.fixture(scope='function')
def payload():
    return CreatePayload.create_payload()


@pytest.fixture(scope='function')
def create_courier(payload):
    return ApiRequestPost.api_request_post(urls.COURIER_REGISTRATION, payload)


@pytest.fixture(scope='function')
def login_data(payload):
    return {
        "login": payload['login'],
        "password": payload['password']
    }
