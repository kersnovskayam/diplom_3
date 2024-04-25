from pages.personal_cabinet_page import PersonalCabinetPage
from utils.allure_decorator import allure_decorator
from utils.constansts import MAIL, PASSWORD
from utils.urls import MAIN_URL, RECOVERY_URL, RESET_PASSWORD_URL


class TestsRecoverUser:

    @allure_decorator("Тест перехода на страницу восстановления пароля")
    def test_click_restore_password(self, browser):
        pc = PersonalCabinetPage(browser)
        pc.open_page(MAIN_URL)
        pc.click_on_personal_cabinet()
        pc.click_on_recover_password()

        assert pc.get_current_page() == RECOVERY_URL

    @allure_decorator("Тест ввода почты и нажатия на кнопку восстановить")
    def test_click_restore(self, browser):
        pc = PersonalCabinetPage(browser)
        pc.open_page(MAIN_URL)
        pc.click_on_personal_cabinet()
        pc.click_on_recover_password()
        pc.send_text_recovery_email(MAIL)
        pc.click_on_recovery_button()

        assert pc.get_current_page() == RECOVERY_URL

    @allure_decorator("Тест скрытия/открытия пароля в поле ввода")
    def test_click_hidden_password(self, browser):
        pc = PersonalCabinetPage(browser)
        pc.open_page(MAIN_URL)
        pc.click_on_personal_cabinet()
        pc.click_on_recover_password()
        pc.send_text_recovery_email(MAIL)
        pc.click_on_recovery_button()
        pc.send_text_recovery_password(PASSWORD)
        pc.click_on_hidden_password()

        assert pc.get_current_page() == RESET_PASSWORD_URL
