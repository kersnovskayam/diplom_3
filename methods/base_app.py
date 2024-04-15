import logging

import requests
from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BaseApp:
    def __init__(self, driver):
        self.driver = driver

    def find_element(self, by, value):
        return self.driver.find_element(by, value)

    def get_page(self, url):
        return self.driver.get(url)

    def check_element_to_be_clickable(self, by, value, timeout=10):
        return WebDriverWait(self.driver, timeout).until(EC.element_to_be_clickable((by, value)))

    def check_visibility_of_element_located(self, by, value, timeout=10):
        return WebDriverWait(self.driver, timeout).until(EC.visibility_of_element_located((by, value)))

    @staticmethod
    def click_on_element(element):
        element.click()

    @staticmethod
    def enter_text(element, text):
        element.send_keys(text)

    @staticmethod
    def send_post_request(url, data):
        try:
            response = requests.post(url, json=data)
            logging.info(f"Отправлен запрос POST по {url}")
            return response
        except requests.exceptions.RequestException as e:
            logging.info(f"Ошибка при отправлении запроса POST по {url}: {e}")
            return None

    def drag_and_drop(self, source_element, target_element):
        actions = ActionChains(self.driver)
        actions.drag_and_drop(source_element, target_element).perform()
