import logging
import random
import string
import requests

from utils.allure_decorator import allure_decorator
from utils.urls import AUTH_REGISTER_ENDPOINT


class OtherMethods:
    @staticmethod
    def generate_random_string(length):
        letters = string.ascii_lowercase
        random_string = ''.join(random.choice(letters) for _ in range(length))
        return random_string

    def generation_data(self):
        email = self.generate_random_string(10)
        password = self.generate_random_string(10)
        name = self.generate_random_string(10)
        email_address = f"{email}@yandex.ru"

        return email_address, password, name

    @allure_decorator("Метод по созданию пользователя")
    def create_user(self, api_connection, email, password, name):
        data = {
            "email": email,
            "password": password,
            "name": name
        }

        response = self.send_post_request(api_connection, data)

        return response

    @allure_decorator("Метод по получению данных по пользователю")
    def return_user_data(self):
        email, password, name = self.generation_data()
        OtherMethods.create_user(AUTH_REGISTER_ENDPOINT, email, password, name)

        return email, password

    @staticmethod
    def send_post_request(url, data):
        try:
            response = requests.post(url, json=data)
            logging.info(f"Отправлен запрос POST по {url}")
            return response
        except requests.exceptions.RequestException as e:
            logging.info(f"Ошибка при отправлении запроса POST по {url}: {e}")
            return None
