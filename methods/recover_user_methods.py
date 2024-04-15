from locators.base_locators import BaseLocators
from locators.personal_cabinet_locators import PersonalCabinetLocators
from methods.base_app import BaseApp
from utils.allure_decorator import allure_decorator


class RecoverUserMethods(BaseApp):

    @allure_decorator("Открываем страницу")
    def open_page(self, url):
        self.get_page(url)

    @allure_decorator("Нажимаем на текст-кнопку личный кабинет")
    def click_element_personal_cabinet(self):
        element = self.check_element_to_be_clickable('xpath', BaseLocators.personal_cabinet_xpath)
        self.click_on_element(element)

    @allure_decorator("Нажимаем на текст-кнопку Восстановить пароль")
    def click_element_recover_password(self):
        element = self.check_element_to_be_clickable('xpath', PersonalCabinetLocators.recover_password_xpath)
        self.click_on_element(element)

    @allure_decorator("Нажимаем на кнопку Восстановить")
    def click_element_recovery_button(self):
        element = self.check_element_to_be_clickable('xpath', PersonalCabinetLocators.recovery_button_xpath)
        self.click_on_element(element)

    @allure_decorator("Вводим текст в поле ввода email")
    def send_text_recovery_email(self, text):
        element = self.check_element_to_be_clickable('xpath', PersonalCabinetLocators.recovery_email_input_xpath)
        self.enter_text(element, text)

    @allure_decorator("Вводим текст в поле ввода пароль")
    def send_text_recovery_password(self, text):
        element = self.check_element_to_be_clickable('xpath', PersonalCabinetLocators.password_recovery_xpath)
        self.enter_text(element, text)

    @allure_decorator("Нажимаем на иконку скрытия/раскрытия пароля")
    def click_element_hidden_password(self):
        element = self.check_element_to_be_clickable('xpath', PersonalCabinetLocators.hide_password_xpath)
        self.click_on_element(element)
