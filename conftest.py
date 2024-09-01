import pytest

import scooter_api
import urls


@pytest.fixture(scope='function')
def payload():
    return scooter_api.create_payload()


@pytest.fixture(scope='function')
def create_courier(payload):
    return scooter_api.api_request(urls.COURIER_REGISTRATION, payload)


@pytest.fixture(scope='function')
def login_data(payload):
    return {
        "login": payload['login'],
        "password": payload['password']
    }

