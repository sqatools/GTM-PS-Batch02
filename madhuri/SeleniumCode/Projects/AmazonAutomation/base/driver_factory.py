from selenium import webdriver
from data.session_data import *


class WebDriverFactory:
    def __init__(self, browser, url):
        self.browser = browser
        self.url = url

    def get_driver(self):
        if self.browser.lower() == 'chrome':
            options = webdriver.ChromeOptions()
            if headless:
                options.add_argument('--headless')
            driver = webdriver.Chrome(options=options)

        elif self.browser.lower() == 'firefox':
            driver = webdriver.Firefox()

        elif self.browser.lower() == 'edge':
            driver = webdriver.Edge()

        driver.get(self.url)
        driver.maximize_window()
        return driver
