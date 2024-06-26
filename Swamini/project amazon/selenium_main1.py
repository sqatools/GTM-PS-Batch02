import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import wait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait

# driver=webdriver.Chrome()
website_url="https://www.amazon.in"

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
    element= wait.until(ec.visibility_of_element_located(locator))
    return element

def click_element(locator):
    element=get_element(locator)
    element.click()

def send_element(data,locator):
    element=get_element(locator)
    element.send_keys(data)

def get_text(locator):
    element = get_element(locator)
    return element.text

def select_dropdown_value(locator, value):
    element = get_element(locator)
    select_obj = Select(element)
    select_obj.select_by_visible_text(value)
