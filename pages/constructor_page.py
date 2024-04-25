from locators.constructor_locators import ConstructorLocators
from pages.base_page import BasePage
from utils.allure_decorator import allure_decorator


class ConstructorPage(BasePage):

    @allure_decorator("Нажатие на раздел конструктор")
    def click_on_constructor(self):
        element = self.check_visibility_of_element_located(ConstructorLocators.constructor_xpath)
        self.click_on_element(element)

    @allure_decorator("Нажатие на ингридиент булка")
    def click_on_ingredient_bun(self):
        element = self.check_visibility_of_element_located(ConstructorLocators.fluorescent_bun)
        self.click_on_element(element)

    @allure_decorator("Нажатие на иконку закрытия модального окна ингридиента")
    def click_on_close_order_button(self):
        element = self.check_visibility_of_element_located(ConstructorLocators.close_button_xpath)
        self.click_on_element(element)

    @allure_decorator("Перемещение булки в конструктор")
    def drag_and_drop_ingredient(self):
        bun_element = self.check_visibility_of_element_located(ConstructorLocators.fluorescent_bun)
        constructor_element = self.check_visibility_of_element_located(ConstructorLocators.constructor_create_burger_locators_xpath)

        self.drag_and_drop(bun_element, constructor_element)

    @allure_decorator("Получение стоимости заказа в конструкторе")
    def get_burger_price(self):
        price_element = self.check_visibility_of_element_located(ConstructorLocators.price_burger_constructor)
        price_text = price_element.text

        return float(price_text)

    @allure_decorator("Нажатие на кнопку оформить заказ")
    def click_on_create_order(self):
        element = self.check_visibility_of_element_located(ConstructorLocators.create_order_xpath)
        self.click_on_element(element)


    @allure_decorator("Получение успешного результата оформления заказа")
    def get_successfully_result_order(self):
        text = self.check_visibility_of_element_located(ConstructorLocators.successfully_order_text_xpath)
        successfully_order_text = text.text

        return successfully_order_text

    @allure_decorator("Получение наименовая булки")
    def get_text_modal_bun(self):
        text = self.check_visibility_of_element_located(ConstructorLocators.fluorescent_bun_text_xpath)
        bun_info_text = text.text

        return bun_info_text
