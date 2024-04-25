from helpers.other_methods import OtherMethods
from pages.constructor_page import ConstructorPage
from pages.list_orders_page import ListOrdersPage
from pages.personal_cabinet_page import PersonalCabinetPage
from utils.allure_decorator import allure_decorator
from utils.constansts import PRICE_ORDER, SUCCESSFULLY_RESULT_ORDER_TEXT, NAME_BUN_MODAL_WINDOW
from utils.urls import MAIN_URL, LIST_ORDERS_URL, BUN_INGREDIENT_URL


class TestsCreateOrder:
    other_method = OtherMethods()

    @allure_decorator("Тест нажатия на страницу конструктор")
    def test_click_constructor(self, browser):
        cr = ConstructorPage(browser)
        ol = ListOrdersPage(browser)

        cr.open_page(MAIN_URL)
        ol.click_on_list_orders()
        cr.click_on_constructor()

        assert cr.get_current_page() == MAIN_URL

    @allure_decorator("Тест нажатия на страницу лента заказов")
    def test_click_list_order(self, browser):
        cr = ConstructorPage(browser)
        ol = ListOrdersPage(browser)

        cr.open_page(MAIN_URL)
        ol.click_on_list_orders()

        assert cr.get_current_page() == LIST_ORDERS_URL

    @allure_decorator("Тест нажатия на ингридиент и проверки отображения модального окна ингридиента")
    def test_click_on_ingredient(self, browser):
        cr = ConstructorPage(browser)

        cr.open_page(MAIN_URL)
        cr.click_on_ingredient_bun()
        ingredient_modal_text = cr.get_text_modal_bun()

        assert ingredient_modal_text == NAME_BUN_MODAL_WINDOW

    @allure_decorator("Тест закрытия модального окна ингридиента")
    def test_click_close_button_ingredient(self, browser):
        cr = ConstructorPage(browser)

        cr.open_page(MAIN_URL)
        cr.click_on_ingredient_bun()
        cr.click_on_close_order_button()

        assert cr.get_current_page() == BUN_INGREDIENT_URL


    @allure_decorator("Тест переноса ингридиента в конструктор заказа и изменение цены в счетчике")
    def test_move_ingredient(self, browser):
        cr = ConstructorPage(browser)

        cr.open_page(MAIN_URL)
        cr.drag_and_drop_ingredient()
        new_price = cr.get_burger_price()

        assert new_price == PRICE_ORDER

    @allure_decorator("Тест оформление заказа под авторизованным пользователем")
    def test_auth_user_order(self, browser):
        cr = ConstructorPage(browser)
        pc = PersonalCabinetPage(browser)

        cr.open_page(MAIN_URL)
        pc.click_on_personal_cabinet()
        email, password = self.other_method.return_user_data()
        pc.send_text_auth_email(email)
        pc.send_text_auth_password(password)
        pc.click_on_input()
        cr.drag_and_drop_ingredient()
        cr.click_on_create_order()
        successfully_order_text = cr.get_successfully_result_order()

        assert successfully_order_text == SUCCESSFULLY_RESULT_ORDER_TEXT
