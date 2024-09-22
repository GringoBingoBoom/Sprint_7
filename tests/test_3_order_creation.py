import allure
import pytest
import urls
from data import ApiMessagesResponse
from helpers import OrderDetails
from scooter_api import ApiRequestPost, ApiRequestGet


class TestOrderCreationAndList:

    @allure.title('3.1 Успешное создание заказа с 4-мя вариантами цвета')
    @pytest.mark.parametrize('color', [["BLACK"], ["GRAY"], ["BLACK", "GRAY"], []])
    def test_success_order_creation(self, color):
        order_details = OrderDetails.create_order_details(color)
        order_request = ApiRequestPost.api_request_post(urls.ORDERS, order_details)

        assert ApiMessagesResponse.message_success_order_creation in order_request['response.text'] and order_request['response.status_code'] == 201

    @allure.title('3.2 Успешное получение списка заказов')
    def test_success_get_list_of_orders(self):
        order_request = ApiRequestGet.api_request_get(urls.ORDERS)
        assert len(order_request['response.text']) > 0 and order_request['response.status_code'] == 200
