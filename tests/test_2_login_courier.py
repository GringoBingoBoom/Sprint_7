import pytest
import scooter_api
import urls

class TestLoginCourier:
    def test_success_login_сourier(self, login_data, create_courier):
        login_request = scooter_api.api_request(urls.COURIER_LOGIN, login_data)
        message = '"id":'
        assert message in login_request['response.text'] and login_request['response.status_code'] == 200

    @pytest.mark.parametrize('missed_field_in_body', ["login", "password"])
    def test_unsuccessful_login_сourier_missed_field(self, login_data, create_courier, missed_field_in_body):
        login_data[missed_field_in_body] = ''
        login_request = scooter_api.api_request(urls.COURIER_LOGIN, login_data)
        message = '"Недостаточно данных для входа"'

        assert message in login_request['response.text'] and login_request['response.status_code'] == 400

    @pytest.mark.parametrize('wrong_data_in_body', ["login", "password"])
    def test_unsuccessful_login_сourier_wrong_data(self, login_data, create_courier, wrong_data_in_body):
        login_data[wrong_data_in_body] = login_data[wrong_data_in_body] + "_1"
        login_request = scooter_api.api_request(urls.COURIER_LOGIN, login_data)
        message = '"Учетная запись не найдена"'

        assert message in login_request['response.text'] and login_request['response.status_code'] == 404
