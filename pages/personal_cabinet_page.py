from locators.personal_cabinet_locators import PersonalCabinetLocators
from pages.base_page import BasePage
from utils.allure_decorator import allure_decorator

class PersonalCabinetPage(BasePage):

    @allure_decorator("Нажимаем на текст-кнопку личный кабинет")
    def click_on_personal_cabinet(self):
        element = self.check_visibility_of_element_located(PersonalCabinetLocators.personal_cabinet_xpath)
        self.click_on_element(element)

    @allure_decorator("Нажимаем на текст-кнопку Восстановить пароль")
    def click_on_recover_password(self):
        element = self.check_visibility_of_element_located(PersonalCabinetLocators.recover_password_xpath)
        self.click_on_element(element)

    @allure_decorator("Нажимаем на кнопку Восстановить")
    def click_on_recovery_button(self):
        element = self.check_visibility_of_element_located(PersonalCabinetLocators.recovery_button_xpath)
        self.click_on_element(element)

    @allure_decorator("Вводим текст в поле ввода email")
    def send_text_recovery_email(self, text):
        element = self.check_visibility_of_element_located(PersonalCabinetLocators.recovery_email_input_xpath)
        self.enter_text(element, text)

    @allure_decorator("Вводим текст в поле ввода пароль")
    def send_text_recovery_password(self, text):
        element = self.check_visibility_of_element_located(PersonalCabinetLocators.password_recovery_xpath)
        self.enter_text(element, text)

    @allure_decorator("Нажимаем на иконку скрытия/раскрытия пароля")
    def click_on_hidden_password(self):
        element = self.check_visibility_of_element_located(PersonalCabinetLocators.hide_password_xpath)
        self.click_on_element(element)

    @allure_decorator("Ввод значения в поле ввода email на экране авторизации")
    def send_text_auth_email(self, text):
        element = self.check_visibility_of_element_located(PersonalCabinetLocators.email_recovery_xpath)
        self.enter_text(element, text)

    @allure_decorator("Ввод значения в поле ввода password на экране авторизации")
    def send_text_auth_password(self, text):
        element = self.check_visibility_of_element_located(PersonalCabinetLocators.password_recovery_xpath)
        self.enter_text(element, text)

    @allure_decorator("Нажатие на кнопку Войти")
    def click_on_input(self):
        element = self.check_visibility_of_element_located(PersonalCabinetLocators.input_button_xpath)
        self.click_on_element(element)

    @allure_decorator("Нажатие на кнопку История заказов")
    def click_on_orders_history(self):
        element = self.check_visibility_of_element_located(PersonalCabinetLocators.orders_history)
        self.click_on_element(element)

    @allure_decorator("Нажатие на кнопку выход")
    def click_on_logout(self):
        element = self.check_visibility_of_element_located(PersonalCabinetLocators.logout_xpath)
        self.click_on_element(element)

    @allure_decorator("Получение номера заказа из раздела история заказов")
    def get_text_number_order(self):
        number_order = self.check_visibility_of_element_located(PersonalCabinetLocators.number_order_in_history_orders).text
        return number_order[1:]
