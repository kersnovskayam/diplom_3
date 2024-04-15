from methods.create_order_methods import CreateOrderMethods
from methods.other_methods import OtherMethods
from utils.allure_decorator import allure_decorator
from utils.constansts import PRICE_ORDER, SUCCESSFULLY_RESULT_ORDER_TEXT, NAME_BUN_MODAL_WINDOW
from utils.urls import MAIN_URL, AUTH_REGISTER_ENDPOINT, LIST_ORDERS_URL, BUN_INGREDIENT_URL


class Tests:

    @allure_decorator("Тест нажатия на страницу конструктор")
    def test_click_constructor(self, browser):
        page = CreateOrderMethods(browser)
        page.open_page(MAIN_URL)
        page.click_on_list_orders()
        page.click_on_constructor()

        assert browser.current_url == MAIN_URL

    @allure_decorator("Тест нажатия на страницу лента заказов")
    def test_click_list_order(self, browser):
        page = CreateOrderMethods(browser)
        page.open_page(MAIN_URL)
        page.click_on_list_orders()

        assert browser.current_url == LIST_ORDERS_URL

    @allure_decorator("Тест нажатия на ингридиент")
    def test_click_on_ingredient(self, browser):
        page = CreateOrderMethods(browser)
        page.open_page(MAIN_URL)
        page.click_on_ingredient_bun()
        ingredient_modal_text = page.get_text_modal_bun()
        assert ingredient_modal_text == NAME_BUN_MODAL_WINDOW



    @allure_decorator("Тест закрытия модального окна ингридиента")
    def test_click_close_button_ingredient(self, browser):
        page = CreateOrderMethods(browser)
        page.open_page(MAIN_URL)
        page.click_on_ingredient_bun()
        page.click_on_close_ingredient()

        assert browser.current_url == BUN_INGREDIENT_URL


    @allure_decorator("Тест переноса ингридиента булочки и изменение цены в счетчике")
    def test_move_ingredient(self, browser):
        page = CreateOrderMethods(browser)
        page.open_page(MAIN_URL)
        page.drag_and_drop_ingredient()
        new_price = page.get_burger_price()

        assert new_price == PRICE_ORDER

    @allure_decorator("")
    def test_auth_user_order(self, browser):
        page = CreateOrderMethods(browser)
        page.open_page(MAIN_URL)
        page.click_on_element_personal_cabinet()
        email, password, name = OtherMethods.generation_data()
        OtherMethods.create_user(AUTH_REGISTER_ENDPOINT, email, password, name)
        page.send_text_auth_email(email)
        page.send_text_auth_password(password)
        page.click_on_element_input()
        page.drag_and_drop_ingredient()
        page.click_on_create_order()
        successfully_order_text = page.get_successfully_result_order()

        assert successfully_order_text == SUCCESSFULLY_RESULT_ORDER_TEXT
