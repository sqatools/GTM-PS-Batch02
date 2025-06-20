import pytest
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
def get_driver(url = website_url, browser=web_browser, timeout= default_timeout):
    if browser.lower() =='chrome':
        global driver
        driver = webdriver.Chrome()
    elif browser.lower() =='firefox':
        driver = webdriver.Firefox()

    global wait
    wait = WebDriverWait(driver, timeout=driver_timeout, poll_frequency=default_poll_frequency)
    driver.maximize_window()
    driver.implicitly_wait(default_implicit_wait)
    driver.get(url)
    return driver, wait


def get_element(locator):
    element = wait.until(ec.visibility_of_element_located(locator))
    return element


def click_element(locator):
    element = get_element(locator)
    element.click()
    return element


def send_data(locator, data):
    element = get_element(locator)
    element.send_keys(data)


def get_text(locator):
    element = get_element(locator)
    return element.text



def move_to_element(locator):
    element = get_element(locator)
    action = ActionChains(driver)
    action.move_to_element(element)
    action.perform()


def click_to_element(locator):
    element = get_element(locator)
    action = ActionChains(driver)
    action.click(element)
    action.perform()