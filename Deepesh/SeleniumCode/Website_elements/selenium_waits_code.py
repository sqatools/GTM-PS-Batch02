import time

from selenium import webdriver
from selenium.webdriver.common.by import By
# from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

"""
implicit wait : This wait will apply on all the web element of the website.
explicit wait : explicit wait will apply on specific element with given condition.
static wait : time.sleep(10) , User has to wait till specified time to move ahead.
"""
website_url = "https://automationbysqatools.blogspot.com/2021/05/dummy-website.html"
wait = None


def get_driver(URL, BROWSER, timeout):
    if BROWSER.lower() == 'chrome':
        driver = webdriver.Chrome()
    elif BROWSER.lower() == 'firefox':
        driver = webdriver.Firefox()
    global wait
    wait = WebDriverWait(driver, timeout, poll_frequency=0.5)
    driver.maximize_window()
    #driver.implicitly_wait(10)
    driver.get(URL)
    #return driver, wait


def get_element(locator):
    element = wait.until(ec.visibility_of_element_located(locator))
    return element


def click_element(locator):
    element = get_element(locator)
    element.click()


def send_data(data, locator):
    element = get_element(locator)
    element.send_keys(data)


def get_text(locator):
    element = get_element(locator)
    return element.text
