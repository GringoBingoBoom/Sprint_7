import pytest
import scooter_api
import urls


class TestOrderCreationAndList:

    @pytest.mark.parametrize('color', [["BLACK"], ["GRAY"], ["BLACK", "GRAY"], []])
    def test_success_order_creation(self, color):
        order_details = scooter_api.create_order_details(color)
        order_request = scooter_api.api_request(urls.ORDERS, order_details)
        message = '"track":'
        assert message in order_request['response.text'] and order_request['response.status_code'] == 201

    def test_success_get_list_of_orders(self):
        order_request = scooter_api.api_request_get(urls.ORDERS)
        assert len(order_request['response.text']) > 0 and order_request['response.status_code'] == 200
