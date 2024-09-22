import allure
import requests
import random
import urls


class ApiRequestPost:
    # метод запроса POST возвращает список из логина, пароля, кода ответа и текст
    @staticmethod
    @allure.step('API запрос POST по BASE_URL+api_url возвращает результат status_code и text')
    def api_request_post(api_url: str, payload: dict) -> dict:
        # отправляем запрос и сохраняем ответ в переменную response
        response = requests.post(urls.BASE_URL + api_url, json=payload)

        # создаём словарь, чтобы метод мог его вернуть
        # добавляем логин и пароль курьера а так же код ответа и текст
        request_and_response_data = payload.copy()
        request_and_response_data['response.status_code'] = response.status_code
        request_and_response_data['response.text'] = response.text

        # возвращаем список
        return request_and_response_data


class ApiRequestGet:
    @staticmethod
    @allure.step('API запрос GET по BASE_URL+api_url возвращает результат status_code и text')
    def api_request_get(api_url: str) -> dict:
        # отправляем запрос на список заказов и сохраняем ответ в переменную response
        url_order_get = f'?limit={random.randint(3, 6)}&nearestStation=["{random.randint(1, 263)}"]'
        response = requests.get(urls.BASE_URL + api_url + url_order_get)

        # создаём словарь, чтобы метод мог его вернуть
        # добавляем код ответа и текст
        response_data = {}
        response_data['response.status_code'] = response.status_code
        response_data['response.text'] = response.json()['orders']

        # возвращаем список
        return response_data
