from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def open_page(self, url):
        return self.driver.get(url)

    def get_current_page(self):
        return self.driver.current_url

    def check_visibility_of_element_located(self, locator):
        return WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located(locator))

    @staticmethod
    def click_on_element(locator):
        locator.click()

    @staticmethod
    def enter_text(locator, text):
        locator.send_keys(text)

    def drag_and_drop(self, source_element, target_element):
        actions = ActionChains(self.driver)
        actions.drag_and_drop(source_element, target_element).perform()
