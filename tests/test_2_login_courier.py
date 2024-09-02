import allure
import pytest

import urls
from scooter_api import ApiRequestPost


class TestLoginCourier:

    @allure.title('2.1 Успешная авторизация курьера')
    def test_success_login_сourier(self, login_data, create_courier):
        login_request = ApiRequestPost.api_request_post(urls.COURIER_LOGIN, login_data)
        message = '"id":'
        assert message in login_request['response.text'] and login_request['response.status_code'] == 200

    @allure.title('2.2 Неуспешная авторизация курьера с пропущенным полем login или password')
    @pytest.mark.parametrize('missed_field_in_body', ["login", "password"])
    def test_unsuccessful_login_сourier_missed_field(self, login_data, create_courier, missed_field_in_body):
        login_data[missed_field_in_body] = ''
        login_request = ApiRequestPost.api_request_post(urls.COURIER_LOGIN, login_data)
        message = '"Недостаточно данных для входа"'

        assert message in login_request['response.text'] and login_request['response.status_code'] == 400

    @allure.title('2.3 Неуспешная авторизация курьера с ошибочным login или password')
    @pytest.mark.parametrize('wrong_data_in_body', ["login", "password"])
    def test_unsuccessful_login_сourier_wrong_data(self, login_data, create_courier, wrong_data_in_body):
        login_data[wrong_data_in_body] = login_data[wrong_data_in_body] + "_1"
        login_request = ApiRequestPost.api_request_post(urls.COURIER_LOGIN, login_data)
        message = '"Учетная запись не найдена"'

        assert message in login_request['response.text'] and login_request['response.status_code'] == 404
