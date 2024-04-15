from locators.base_locators import BaseLocators
from locators.create_order_locators import CreateOrderLocators
from locators.personal_cabinet_locators import PersonalCabinetLocators
from methods.base_app import BaseApp
from utils.allure_decorator import allure_decorator


class CreateOrderMethods(BaseApp):

    @allure_decorator("Открываем страницу")
    def open_page(self, url):
        self.get_page(url)

    @allure_decorator("Нажатие на раздел лента заказов")
    def click_on_list_orders(self):
        element = self.check_element_to_be_clickable('xpath', BaseLocators.list_order_xpath)
        self.click_on_element(element)

    @allure_decorator("Нажатие на раздел конструктор")
    def click_on_constructor(self):
        element = self.check_element_to_be_clickable('xpath', BaseLocators.constructor_xpath)
        self.click_on_element(element)

    @allure_decorator("Нажатие на ингридиент булка")
    def click_on_ingredient_bun(self):
        element = self.check_element_to_be_clickable('xpath', CreateOrderLocators.fluorescent_bun)
        self.click_on_element(element)

    @allure_decorator("Нажатие на иконку закрытия модального окна ингридиента")
    def click_on_close_ingredient(self):
        element = self.check_element_to_be_clickable('xpath', CreateOrderLocators.close_button_xpath)
        self.click_on_element(element)

    @allure_decorator("Перемещение булки в конструктор")
    def drag_and_drop_ingredient(self):
        bun_element = self.check_element_to_be_clickable('xpath', CreateOrderLocators.fluorescent_bun)
        constructor_element = self.check_visibility_of_element_located('xpath',
                                                                       CreateOrderLocators.constructor_create_burger_locators_xpath)

        self.drag_and_drop(bun_element, constructor_element)

    @allure_decorator("Получение стоимости заказа в конструкторе")
    def get_burger_price(self):
        price_element = self.check_visibility_of_element_located('xpath', CreateOrderLocators.price_burger_constructor)
        price_text = price_element.text

        return float(price_text)

    @allure_decorator("Нажатие на кнопку оформить заказ")
    def click_on_create_order(self):
        element = self.check_element_to_be_clickable('xpath', CreateOrderLocators.create_order_xpath)
        self.click_on_element(element)

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

    @allure_decorator("Получение успешного результата оформления заказа")
    def get_successfully_result_order(self):
        text = self.check_visibility_of_element_located('xpath', CreateOrderLocators.successfully_order_text_xpath)
        successfully_order_text = text.text

        return successfully_order_text

    @allure_decorator("Получение наименовая булки")
    def get_text_modal_bun(self):
        text = self.check_visibility_of_element_located('xpath', CreateOrderLocators.fluorescent_bun_text_xpath)
        bun_info_text = text.text

        return bun_info_text
