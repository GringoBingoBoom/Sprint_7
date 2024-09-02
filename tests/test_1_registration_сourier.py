import allure
import pytest

from helpers import CreatePayload
from scooter_api import ApiRequestPost
import urls


class TestRegistrationCourier:

    @allure.title('1.1 Успешная регистрация курьера')
    def test_success_registration_сourier(self, payload):
        registration_request = ApiRequestPost.api_request_post(urls.COURIER_REGISTRATION, payload)
        assert registration_request['response.status_code'] == 201 and registration_request[
            'response.text'] == '{"ok":true}', 'Неуспешная регистрация курьера'

    @allure.title('1.2 Неуспешная регистрация 2-х одинаковых курьеров')
    def test_unsuccessful_registration_two_same_сourier(self, payload):
        registration_request = ApiRequestPost.api_request_post(urls.COURIER_REGISTRATION, payload)
        registration_request = ApiRequestPost.api_request_post(urls.COURIER_REGISTRATION, payload)
        message = '"message":"Этот логин уже используется'

        assert message in registration_request['response.text']

    @allure.title('1.3 Неуспешная регистрация курьера с пропушенным полем login или password')
    @pytest.mark.parametrize('missed_field_in_body', ["login", "password"])
    def test_unsuccessful_registration_сourier_with_missed_field_in_body(self, missed_field_in_body, payload):
        payload[missed_field_in_body] = ''
        registration_request = ApiRequestPost.api_request_post(urls.COURIER_REGISTRATION, payload)
        message = '"message":"Недостаточно данных для создания учетной записи"'

        assert message in registration_request['response.text']

    @allure.title('1.4 Неуспешная регистрация курьеров с одинаковым полем login')
    def test_unsuccessful_registration_two_same_login_сourier(self, payload):
        payload_2nd = CreatePayload.create_payload()
        payload_2nd['login'] = payload['login']
        registration_request = ApiRequestPost.api_request_post(urls.COURIER_REGISTRATION, payload)
        registration_request_2nd = ApiRequestPost.api_request_post(urls.COURIER_REGISTRATION, payload_2nd)
        message = '"message":"Этот логин уже используется'

        assert message in registration_request_2nd['response.text']
