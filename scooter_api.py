import allure
import requests
import random
import string
import urls


# метод запроса POST возвращает список из логина, пароля, кода ответа и текст
@allure.step('API запрос POST по BASE_URL+api_url возвращает результат status_code и text')
def api_request(api_url: str, payload: dict) -> dict:
    # отправляем запрос и сохраняем ответ в переменную response
    response = requests.post(urls.BASE_URL + api_url, json=payload)

    # создаём словарь, чтобы метод мог его вернуть
    # добавляем логин и пароль курьера а так же код ответа и текст
    request_and_response_data = payload.copy()
    request_and_response_data['response.status_code'] = response.status_code
    request_and_response_data['response.text'] = response.text

    # возвращаем список
    return request_and_response_data


# метод генерирует строку, состоящую только из букв нижнего регистра, в качестве параметра передаём длину строки
@allure.step('Генерируем случайную символьную строку')
def generate_random_string(length: int) -> str:
    letters = string.ascii_lowercase
    random_string = ''.join(random.choice(letters) for i in range(length))
    return random_string


@allure.step('Создаем случайные данные login, password, firstName')
def create_payload() -> dict:
    # генерируем логин, пароль и имя курьера
    login = generate_random_string(10)
    password = generate_random_string(10)
    first_name = generate_random_string(10)

    payload = {
        "login": login,
        "password": password,
        "firstName": first_name
    }

    return payload

@allure.step('Создаем случайные данные для нового заказа')
def create_order_details(color: list = []) -> dict:
    order_details = {
        "firstName": generate_random_string(10),
        "lastName": generate_random_string(10),
        "address": generate_random_string(10),
        "metroStation": random.randint(1, 263),
        "phone": str(random.randint(70010000001, 79999999999)),
        "rentTime": random.randint(1, 10),
        "deliveryDate": f"2024-{random.randint(10, 12)}-{random.randint(1, 30)}",
        "comment": generate_random_string(10),
        "color": color
    }
    return order_details

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

