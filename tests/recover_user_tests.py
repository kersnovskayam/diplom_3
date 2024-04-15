from methods.recover_user_methods import RecoverUserMethods
from utils.allure_decorator import allure_decorator
from utils.constansts import MAIL, PASSWORD
from utils.urls import MAIN_URL, RECOVERY_URL, RESET_PASSWORD_URL


class Tests:

    @allure_decorator("Тест перехода на страницу восстановления пароля")
    def test_click_restore_password(self, browser):
        page = RecoverUserMethods(browser)
        page.open_page(MAIN_URL)
        page.click_element_personal_cabinet()
        page.click_element_recover_password()

        assert browser.current_url == RECOVERY_URL


    @allure_decorator("Тест ввода почты и нажатия на кнопку восстановить")
    def test_click_restore(self, browser):
        page = RecoverUserMethods(browser)
        page.open_page(MAIN_URL)
        page.click_element_personal_cabinet()
        page.click_element_recover_password()
        page.send_text_recovery_email(MAIL)
        page.click_element_recovery_button()

        assert browser.current_url == RECOVERY_URL


    @allure_decorator("Тест скрытия/открытия пароля в поле ввода")
    def test_click_hidden_password(self, browser):
        page = RecoverUserMethods(browser)
        page.open_page(MAIN_URL)
        page.click_element_personal_cabinet()
        page.click_element_recover_password()
        page.send_text_recovery_email(MAIL)
        page.click_element_recovery_button()
        page.send_text_recovery_password(PASSWORD)
        page.click_element_hidden_password()

        assert browser.current_url == RESET_PASSWORD_URL
