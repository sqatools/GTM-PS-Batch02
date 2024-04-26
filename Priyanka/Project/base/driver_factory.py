from selenium import webdriver
from data.session_data import *

class WebDriverFactory:

    def __init__(self, Browser, Url):
        self.browser = Browser
        self.URL = Url

    def get_driver(self):
        if self.browser.lower() == "chrome":
            driver = webdriver.Chrome()

        elif self.browser.lower() == "firefox":
            #driver = webdriver.Firefox()
            options = webdriver.ChromeOptions()
            if headless:
                options.add_argument('--headless')
                driver = webdriver.Firefox(options=options)

        elif self.browser.lower() == "edge":
            driver = webdriver.Edge()

        driver.get(self.URL)
        driver.maximize_window()
        return driver

