import pytest
import time

from selenium import webdriver
from selenium.webdriver.common.by import By

import time
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.action_chains import ActionChains

# custom file
from config import *

wait = None
driver = None


@pytest.fixture(scope="function")
def setup():
    def get_driver(url=website_url, browser=web_browser, timeout=default_timeout):
        if browser.lower() == 'chrome':
            global driver
            driver = webdriver.Chrome()
        elif browser.lower() == 'firefox':
            driver = webdriver.Firefox()

        global wait
        wait = WebDriverWait(driver, timeout=driver_timeout, poll_frequency=default_poll_frequency)
        driver.maximize_window()
        driver.implicitly_wait(default_implicit_wait)
        driver.get(url)
        return driver, wait


@pytest.fixture(scope="session",autouse=True)
def greeting():
    print("-"*50,"Welcome to Amazon Test Suit", "*"*50)
    yield
    print("-"*50,"Pytest Execution has been completed", "*"*50)


