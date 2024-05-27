import time
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait

website_url="https://automationbysqatools.blogspot.com/2021/05/dummy-website.html"
Wait = None


def get_driver(URL=website_url, BROWSER='chrome',timeout=15):
    global Wait
    if BROWSER.lower() =='chrome':
        driver = webdriver.Chrome()
    elif BROWSER.lower() == 'firefox':
        driver = webdriver.Firefox()
    Wait = WebDriverWait(driver, timeout, poll_frequency=0.5)
    driver.maximize_window()
    driver.get(URL)
    return driver,Wait

def click_element(locator):
    element=Wait.until(ec.visibility_of_element_located(locator))
    element.click()

def send_data(data,locator):
    element=Wait.until(ec.visibility_of_element_located(locator))
    element.send_keys(data)

def get_element(locator):
    element= Wait.until(ec.visibility_of_element_located(locator))
    return element

def click_element(locator):
    element=get_element(locator)
    element.click()

def send_keys(data,locator):
    element=get_element(locator)
    element.send_keys(data)

def get_text(locator):
    element=get_element(locator)
    return element.text
