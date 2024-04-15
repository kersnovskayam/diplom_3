from locators.base_locators import BaseLocators
from locators.personal_cabinet_locators import PersonalCabinetLocators
from methods.base_app import BaseApp
from utils.allure_decorator import allure_decorator


class PersonalCabinetMethods(BaseApp):

    @allure_decorator("Открываем страницу")
    def open_page(self, url):
        self.get_page(url)

    @allure_decorator("Нажимаем на текст-кнопку личный кабинет")
    def click_on_element_personal_cabinet(self):
        element = self.check_element_to_be_clickable('xpath', BaseLocators.personal_cabinet_xpath)
        self.click_on_element(element)

    @allure_decorator("Ввод значения в поле ввода email на экране авторизации")
    def send_text_auth_email(self, text):
        element = self.check_element_to_be_clickable('xpath', PersonalCabinetLocators.email_recovery_xpath)
        self.enter_text(element, text)

    @allure_decorator("Ввод значения в поле ввода password на экране авторизации")
    def send_text_auth_password(self, text):
        element = self.check_element_to_be_clickable('xpath', PersonalCabinetLocators.password_recovery_xpath)
        self.enter_text(element, text)

    @allure_decorator("Нажатие на кнопку Войти")
    def click_on_element_input(self):
        element = self.check_element_to_be_clickable('xpath', PersonalCabinetLocators.input_button_xpath)
        self.click_on_element(element)

    @allure_decorator("Нажатие на кнопку История заказов")
    def click_on_element_orders_history(self):
        element = self.check_element_to_be_clickable('xpath', PersonalCabinetLocators.orders_history)
        self.click_on_element(element)

    @allure_decorator("Нажатие на кнопку выход")
    def click_on_element_logout(self):
        element = self.check_element_to_be_clickable('xpath', PersonalCabinetLocators.logout_xpath)
        self.click_on_element(element)
