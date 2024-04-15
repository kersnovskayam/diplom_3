import pytest
from selenium import webdriver
from selenium.webdriver.firefox.options import Options

# раздокументировать для теста в FireFox
# @pytest.fixture(scope="function", autouse=True)
# def browser(request):
#     options = Options()
#     options.headless = False
#     driver = webdriver.Firefox()
#     driver.implicitly_wait(100)
#     yield driver
#     driver.quit()

@pytest.fixture(scope="function", autouse=True)
def browser(request):
    options = Options()
    options.headless = False
    driver = webdriver.Chrome()
    driver.implicitly_wait(100)
    yield driver
    driver.quit()
