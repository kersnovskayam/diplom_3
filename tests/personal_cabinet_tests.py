from methods.other_methods import OtherMethods
from methods.personal_cabinet_methods import PersonalCabinetMethods
from utils.allure_decorator import allure_decorator
from utils.urls import MAIN_URL, PERSONAL_CABINET_LOGIN_URL, AUTH_REGISTER_ENDPOINT, ORDERS_HISTORY_URL, \
    PROFILE_CABINET_URL


class Tests:

    @allure_decorator("Тест перехода на страницу восстановления пароля")
    def test_click_restore_password(self, browser):
        page = PersonalCabinetMethods(browser)
        page.open_page(MAIN_URL)
        page.click_on_element_personal_cabinet()

        assert browser.current_url == PERSONAL_CABINET_LOGIN_URL

    @allure_decorator("Тест перехода на страницу восстановления пароля")
    def test_click_orders_history(self, browser):
        page = PersonalCabinetMethods(browser)
        page.open_page(MAIN_URL)
        page.click_on_element_personal_cabinet()
        email, password, name = OtherMethods.generation_data()
        OtherMethods.create_user(AUTH_REGISTER_ENDPOINT, email, password, name)
        page.send_text_auth_email(email)
        page.send_text_auth_password(password)
        page.click_on_element_input()
        page.click_on_element_personal_cabinet()
        page.click_on_element_orders_history()

        assert browser.current_url == ORDERS_HISTORY_URL

    @allure_decorator("Тест перехода на страницу восстановления пароля")
    def test_click_logout(self, browser):
        page = PersonalCabinetMethods(browser)
        page.open_page(MAIN_URL)
        page.click_on_element_personal_cabinet()
        email, password, name = OtherMethods.generation_data()
        OtherMethods.create_user(AUTH_REGISTER_ENDPOINT, email, password, name)
        page.send_text_auth_email(email)
        page.send_text_auth_password(password)
        page.click_on_element_input()
        page.click_on_element_personal_cabinet()
        page.click_on_element_logout()

        assert browser.current_url == PROFILE_CABINET_URL
