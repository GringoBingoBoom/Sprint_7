import string
import random

import allure


class CreatePayload:
    # метод генерирует строку, состоящую только из букв нижнего регистра, в качестве параметра передаём длину строки
    @staticmethod
    @allure.step('Генерируем случайную символьную строку')
    def generate_random_string(length: int) -> str:
        letters = string.ascii_lowercase
        random_string = ''.join(random.choice(letters) for i in range(length))
        return random_string

    @staticmethod
    @allure.step('Создаем случайные данные login, password, firstName')
    def create_payload() -> dict:
        # генерируем логин, пароль и имя курьера
        login = CreatePayload.generate_random_string(10)
        password = CreatePayload.generate_random_string(10)
        first_name = CreatePayload.generate_random_string(10)

        payload = {
            "login": login,
            "password": password,
            "firstName": first_name
        }

        return payload


class OrderDetails:
    @staticmethod
    @allure.step('Создаем случайные данные для нового заказа')
    def create_order_details(color: list = []) -> dict:
        order_details = {
            "firstName": CreatePayload.generate_random_string(10),
            "lastName": CreatePayload.generate_random_string(10),
            "address": CreatePayload.generate_random_string(10),
            "metroStation": random.randint(1, 263),
            "phone": str(random.randint(70010000001, 79999999999)),
            "rentTime": random.randint(1, 10),
            "deliveryDate": f"2024-{random.randint(10, 12)}-{random.randint(1, 30)}",
            "comment": CreatePayload.generate_random_string(10),
            "color": color
        }
        return order_details
