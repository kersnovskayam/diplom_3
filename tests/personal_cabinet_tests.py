from helpers.other_methods import OtherMethods
from pages.personal_cabinet_page import PersonalCabinetPage
from utils.allure_decorator import allure_decorator
from utils.urls import MAIN_URL, PERSONAL_CABINET_LOGIN_URL, ORDERS_HISTORY_URL, \
    PROFILE_CABINET_URL


class TestsPersonalCabinet:

    other_method = OtherMethods()

    @allure_decorator("Тест перехода на страницу личный кабинет")
    def test_click_restore_password(self, browser):
        pc = PersonalCabinetPage(browser)
        pc.open_page(MAIN_URL)
        pc.click_on_personal_cabinet()

        assert pc.get_current_page() == PERSONAL_CABINET_LOGIN_URL

    @allure_decorator("Тест перехода на страницу история заказов")
    def test_click_orders_history(self, browser):
        pc = PersonalCabinetPage(browser)
        pc.open_page(MAIN_URL)
        pc.click_on_personal_cabinet()
        email, password, name = self.other_method.generation_data()
        pc.send_text_auth_email(email)
        pc.send_text_auth_password(password)
        pc.click_on_input()
        pc.click_on_personal_cabinet()
        pc.click_on_orders_history()

        assert pc.get_current_page() == ORDERS_HISTORY_URL

    @allure_decorator("Тест выхода из аккаунта")
    def test_click_logout(self, browser):
        pc = PersonalCabinetPage(browser)
        pc.open_page(MAIN_URL)
        pc.click_on_personal_cabinet()
        email, password, name = self.other_method.generation_data()
        pc.send_text_auth_email(email)
        pc.send_text_auth_password(password)
        pc.click_on_input()
        pc.click_on_personal_cabinet()
        pc.click_on_logout()

        assert pc.get_current_page() == PROFILE_CABINET_URL