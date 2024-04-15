import random
import string

from methods.base_app import BaseApp
from utils.allure_decorator import allure_decorator


class OtherMethods:
    @staticmethod
    def generate_random_string(length):
        letters = string.ascii_lowercase
        random_string = ''.join(random.choice(letters) for _ in range(length))
        return random_string

    @staticmethod
    def generation_data():
        email = OtherMethods.generate_random_string(10)
        password = OtherMethods.generate_random_string(10)
        name = OtherMethods.generate_random_string(10)
        email_address = f"{email}@yandex.ru"

        return email_address, password, name

    @staticmethod
    @allure_decorator("Метод по созданию пользователя")
    def create_user(api_connection, email, password, name):
        data = {
            "email": email,
            "password": password,
            "name": name
        }

        response = BaseApp.send_post_request(api_connection, data)

        return response
