from locators.list_orders_locators import ListOrderLocators
from locators.personal_cabinet_locators import PersonalCabinetLocators
from pages.base_page import BasePage

from utils.allure_decorator import allure_decorator


class ListOrdersPage(BasePage):

    @allure_decorator("Нажатие на раздел лента заказов")
    def click_on_list_orders(self):
        element = self.check_visibility_of_element_located(ListOrderLocators.list_order_xpath)
        self.click_on_element(element)

    @allure_decorator("нажатия на заказ")
    def click_on_order_in_list(self):
        element = self.check_visibility_of_element_located(ListOrderLocators.order_in_list_xpath)
        self.click_on_element(element)

    @allure_decorator("Получение номера заказа из раздела история заказов")
    def get_text_number_order(self):
        number_order = self.check_visibility_of_element_located(PersonalCabinetLocators.number_order_in_history_orders).text
        return number_order[1:]

    @allure_decorator("Получение номера заказа из ленты заказов")
    def get_text_number_in_order_list(self):
        order_text = self.check_visibility_of_element_located(ListOrderLocators.order_in_list_xpath).text
        order_text_lines = order_text.split('\n')
        order_number_str = order_text_lines[0]
        order_number = order_number_str[1:]
        return order_number

    @allure_decorator("Получение количества заказов за все время из ленты заказов")
    def get_text_all_orders(self):
        text = self.check_visibility_of_element_located(ListOrderLocators.count_all_orders_xpath).text
        count_all_orders = int(text)
        return count_all_orders

    @allure_decorator("Получение количества заказов за сегодня из ленты заказов")
    def get_text_today_orders(self):
        text = self.check_visibility_of_element_located(ListOrderLocators.count_today_orders_xpath).text
        count_today_orders = int(text)
        return count_today_orders

    @allure_decorator("Получение заказов находящегося в работе")
    def get_text_work_order(self):
        text = self.check_visibility_of_element_located(ListOrderLocators.orders_in_work_xpath).text
        return text

    @allure_decorator("Получение текста состава из модального окна заказа")
    def get_text_compound_in_modal_window(self):
        text = self.check_visibility_of_element_located(ListOrderLocators.compound_in_modal_window_xpath).text
        return text
