import time

from helpers.other_methods import OtherMethods
from pages.constructor_page import ConstructorPage
from pages.list_orders_page import ListOrdersPage
from pages.personal_cabinet_page import PersonalCabinetPage
from utils.allure_decorator import allure_decorator
from utils.constansts import COMPOUND
from utils.urls import MAIN_URL

class Tests:

    other_method = OtherMethods()

    @allure_decorator("Тест открытия модального окна заказа в ленте заказов")
    def test_click_order_in_list_order(self, browser):
        ls = ListOrdersPage(browser)

        ls.open_page(MAIN_URL)
        ls.click_on_list_orders()
        ls.click_on_order_in_list()
        compound = ls.get_text_compound_in_modal_window()

        assert compound == COMPOUND

    @allure_decorator("Тест проверки отображения оформленного заказа из истории заказов в ленте заказов")
    def test_create_order_in_history_orders_and_list_orders(self, browser):
        lo = ListOrdersPage(browser)
        pc = PersonalCabinetPage(browser)
        ct = ConstructorPage(browser)

        lo.open_page(MAIN_URL)
        pc.click_on_personal_cabinet()
        email, password = self.other_method.return_user_data()
        pc.send_text_auth_email(email)
        pc.send_text_auth_password(password)
        pc.click_on_input()
        ct.drag_and_drop_ingredient()
        ct.click_on_create_order()
        ct.click_on_close_order_button()
        pc.click_on_personal_cabinet()
        pc.click_on_orders_history()
        order_in_history_orders = pc.get_text_number_order()
        lo.click_on_list_orders()
        order_in_list_orders = lo.get_text_number_in_order_list()

        assert order_in_history_orders == order_in_list_orders

    @allure_decorator("Тест проверки изменения количества всех заказов")
    def test_count_all_orders_in_list_orders(self, browser):
        lo = ListOrdersPage(browser)
        pc = PersonalCabinetPage(browser)
        ct = ConstructorPage(browser)

        lo.open_page(MAIN_URL)
        pc.click_on_personal_cabinet()
        email, password = self.other_method.return_user_data()
        pc.send_text_auth_email(email)
        pc.send_text_auth_password(password)
        pc.click_on_input()
        lo.click_on_list_orders()
        count = lo.get_text_all_orders()
        old_count = count + 1
        ct.click_on_constructor()
        ct.drag_and_drop_ingredient()
        ct.click_on_create_order()
        ct.click_on_close_order_button()
        lo.click_on_list_orders()
        update_count = lo.get_text_all_orders()

        assert old_count == update_count

    @allure_decorator("Тест проверки изменения количества заказов за сегодня")
    def test_count_today_orders_is_list_orders(self, browser):
        lo = ListOrdersPage(browser)
        pc = PersonalCabinetPage(browser)
        ct = ConstructorPage(browser)

        lo.open_page(MAIN_URL)
        pc.click_on_personal_cabinet()
        email, password = self.other_method.return_user_data()
        pc.send_text_auth_email(email)
        pc.send_text_auth_password(password)
        pc.click_on_input()
        lo.click_on_list_orders()
        count = lo.get_text_today_orders()
        old_count = count + 1
        ct.click_on_constructor()
        ct.drag_and_drop_ingredient()
        ct.click_on_create_order()
        ct.click_on_close_order_button()
        lo.click_on_list_orders()
        update_count = lo.get_text_today_orders()

        assert old_count == update_count

    @allure_decorator("Тест проверки отображения номера заказа в статусе в работе")
    def test_order_number_in_work(self, browser):
        lo = ListOrdersPage(browser)
        pc = PersonalCabinetPage(browser)
        ct = ConstructorPage(browser)

        lo.open_page(MAIN_URL)
        pc.click_on_personal_cabinet()
        email, password = self.other_method.return_user_data()
        pc.send_text_auth_email(email)
        pc.send_text_auth_password(password)
        pc.click_on_input()
        ct.drag_and_drop_ingredient()
        ct.click_on_create_order()
        ct.click_on_close_order_button()
        pc.click_on_personal_cabinet()
        pc.click_on_orders_history()
        order_in_history_orders = pc.get_text_number_order()
        lo.click_on_list_orders()
        time.sleep(3)
        order_in_work = lo.get_text_work_order()

        assert order_in_history_orders == order_in_work