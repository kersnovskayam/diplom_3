import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions



@pytest.fixture(scope='function', params=['chrome', 'firefox'])
def browser(request):
    driver_type = request.param

    if driver_type == 'chrome':
        chrome_options = ChromeOptions()
        chrome_options.add_argument("--window-size=1920,1080")
        chrome_options.add_argument("pageLoadStrategy=normal")
        driver = webdriver.Chrome(options=chrome_options)
    elif driver_type == 'firefox':
        firefox_options = FirefoxOptions()
        firefox_options.add_argument("--width=1920")
        firefox_options.add_argument("--height=1080")
        firefox_options.set_preference("pageLoadStrategy", "normal")
        driver = webdriver.Firefox(options=firefox_options)
    else:
        raise ValueError(f"Unsupported browser: {driver_type}")

    yield driver
    driver.quit()

