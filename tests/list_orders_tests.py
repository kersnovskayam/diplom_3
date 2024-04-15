from methods.list_orders_methods import ListOrdersMethods
from methods.other_methods import OtherMethods
from utils.allure_decorator import allure_decorator
from utils.urls import MAIN_URL, AUTH_REGISTER_ENDPOINT


class Tests:

    @allure_decorator("Тест нажатия на страницу лента заказов")
    def test_click_order_in_list_order(self, browser):
        page = ListOrdersMethods(browser)
        page.open_page(MAIN_URL)
        page.click_on_list_orders()
        page.click_on_order_in_list()


    @allure_decorator("Тест проверки что заказ из истории заказов отображается в ленте заказов")
    def test_create_order_in_history_orders_and_list_orders(self, browser):
        page = ListOrdersMethods(browser)
        page.open_page(MAIN_URL)
        page.click_on_element_personal_cabinet()
        email, password, name = OtherMethods.generation_data()
        OtherMethods.create_user(AUTH_REGISTER_ENDPOINT, email, password, name)
        page.send_text_auth_email(email)
        page.send_text_auth_password(password)
        page.click_on_element_input()
        page.drag_and_drop_ingredient()
        page.click_on_create_order()
        page.click_on_close_order()
        page.click_on_element_personal_cabinet()
        page.click_on_history_orders()
        order_in_history_orders = page.get_text_number_order()
        page.click_on_list_orders()
        order_in_list_orders = page.get_text_number_in_order_list()

        assert order_in_history_orders == order_in_list_orders

    @allure_decorator("Тест проверки изменения количества всех заказов")
    def test_count_all_orders_in_list_orders(self, browser):
        page = ListOrdersMethods(browser)
        page.open_page(MAIN_URL)
        page.click_on_element_personal_cabinet()
        email, password, name = OtherMethods.generation_data()
        OtherMethods.create_user(AUTH_REGISTER_ENDPOINT, email, password, name)
        page.send_text_auth_email(email)
        page.send_text_auth_password(password)
        page.click_on_element_input()
        page.click_on_list_orders()
        count = page.get_text_all_orders()
        old_count = count + 1
        page.click_on_constructor()
        page.drag_and_drop_ingredient()
        page.click_on_create_order()
        page.click_on_close_order()
        page.click_on_list_orders()
        update_count = page.get_text_all_orders()

        assert old_count == update_count

    @allure_decorator("Тест проверки изменения количества всех заказов")
    def test_count_today_orders_is_list_orders(self, browser):
        page = ListOrdersMethods(browser)
        page.open_page(MAIN_URL)
        page.click_on_element_personal_cabinet()
        email, password, name = OtherMethods.generation_data()
        OtherMethods.create_user(AUTH_REGISTER_ENDPOINT, email, password, name)
        page.send_text_auth_email(email)
        page.send_text_auth_password(password)
        page.click_on_element_input()
        page.click_on_list_orders()
        count = page.get_text_today_orders()
        old_count = count + 1
        page.click_on_constructor()
        page.drag_and_drop_ingredient()
        page.click_on_create_order()
        page.click_on_close_order()
        page.click_on_list_orders()
        update_count = page.get_text_today_orders()

        assert old_count == update_count

    @allure_decorator("Тест проверки изменения количества всех заказов")
    def test_order_number_in_work(self, browser):
        page = ListOrdersMethods(browser)
        page.open_page(MAIN_URL)
        page.click_on_element_personal_cabinet()
        email, password, name = OtherMethods.generation_data()
        OtherMethods.create_user(AUTH_REGISTER_ENDPOINT, email, password, name)
        page.send_text_auth_email(email)
        page.send_text_auth_password(password)
        page.click_on_element_input()
        page.drag_and_drop_ingredient()
        page.click_on_create_order()
        page.click_on_close_order()
        page.click_on_element_personal_cabinet()
        page.click_on_history_orders()
        page.click_on_element_personal_cabinet()
        page.click_on_history_orders()
        order_in_history_orders = page.get_text_number_order()
        page.click_on_list_orders()
        order_in_work = page.get_text_work_order()

        assert order_in_history_orders == order_in_work
