from locators.base_locators import BaseLocators
from locators.create_order_locators import CreateOrderLocators
from locators.list_orders_locators import ListOrderLocators
from locators.personal_cabinet_locators import PersonalCabinetLocators
from methods.base_app import BaseApp
from utils.allure_decorator import allure_decorator


class ListOrdersMethods(BaseApp):

    @allure_decorator("Открываем страницу")
    def open_page(self, url):
        self.get_page(url)

    @allure_decorator("Нажатие на раздел лента заказов")
    def click_on_list_orders(self):
        element = self.check_element_to_be_clickable('xpath', BaseLocators.list_order_xpath)
        self.click_on_element(element)

    @allure_decorator("нажатия на заказ")
    def click_on_order_in_list(self):
        element = self.check_element_to_be_clickable('xpath', ListOrderLocators.order_in_list_xpath)
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

    @allure_decorator("Перемещение булки в конструктор")
    def drag_and_drop_ingredient(self):
        bun_element = self.check_element_to_be_clickable('xpath', CreateOrderLocators.fluorescent_bun)
        constructor_element = self.check_visibility_of_element_located('xpath',
                                                                       CreateOrderLocators.constructor_create_burger_locators_xpath)

        self.drag_and_drop(bun_element, constructor_element)

    @allure_decorator("Нажатие на кнопку оформить заказ")
    def click_on_create_order(self):
        element = self.check_element_to_be_clickable('xpath', CreateOrderLocators.create_order_xpath)
        self.click_on_element(element)

    @allure_decorator("Нажатие на кнопку закрыть")
    def click_on_close_order(self):
        element = self.check_visibility_of_element_located('xpath', CreateOrderLocators.close_order_button_xpath)
        self.click_on_element(element)

    @allure_decorator("Получение номера заказа из раздела история заказов")
    def get_text_number_order(self):
        number_order = self.check_visibility_of_element_located('xpath', PersonalCabinetLocators.number_order_in_history_orders).text
        return number_order[1:]

    @allure_decorator("Нажимаем на текст-кнопку личный кабинет")
    def click_on_element_personal_cabinet(self):
        element = self.check_element_to_be_clickable('xpath', BaseLocators.personal_cabinet_xpath)
        self.click_on_element(element)

    @allure_decorator("Нажимаем на раздел История заказов")
    def click_on_history_orders(self):
        element = self.check_visibility_of_element_located('xpath', PersonalCabinetLocators.orders_history)
        self.click_on_element(element)


    @allure_decorator("Получение номера заказа из ленты заказов")
    def get_text_number_in_order_list(self):
        order_number = self.check_visibility_of_element_located('xpath', ListOrderLocators.number_order_in_list_order_xpath).text
        return order_number[1:]

    @allure_decorator("Нажатие на раздел конструктор")
    def click_on_constructor(self):
        element = self.check_element_to_be_clickable('xpath', BaseLocators.constructor_xpath)
        self.click_on_element(element)

    @allure_decorator("Получение количества заказов за все время из ленты заказов")
    def get_text_all_orders(self):
        text = self.check_visibility_of_element_located('xpath', ListOrderLocators.count_all_orders_xpath).text
        count_all_orders = int(text)
        return count_all_orders

    @allure_decorator("Получение количества заказов за сегодня из ленты заказов")
    def get_text_today_orders(self):
        text = self.check_visibility_of_element_located('xpath', ListOrderLocators.count_today_orders_xpath).text
        count_today_orders = int(text)
        return count_today_orders

    @allure_decorator("Получение заказов находящегося в работе")
    def get_text_work_order(self):
        number_work_order = self.check_visibility_of_element_located('xpath', ListOrderLocators.orders_in_work_xpath).text
        return number_work_order
