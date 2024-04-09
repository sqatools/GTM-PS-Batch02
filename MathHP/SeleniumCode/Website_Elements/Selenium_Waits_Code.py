import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

website_url = "https://automationbysqatools.blogspot.com/2021/05/dummy-website.html"
wait = None
def get_driver(URL=website_url,BROWSER='chrome',timeout=15):
    if BROWSER.lower() == 'chrome':
        driver = webdriver.Chrome()
    elif BROWSER.lower() == 'Firefox':
        driver = webdriver.Firefox()
    global wait
    wait = WebDriverWait(driver, 15, poll_frequency=0.5)
    driver.implicitly_wait(10)
    driver.maximize_window()
    driver.get(URL)                                 # Not wait for page to get loaded
    return driver,wait

def get_element(locator):
    element = wait.until(expected_conditions.visibility_of_element_located(locator))
    return element

def click_element(locator):
    element = wait.until(expected_conditions.visibility_of_element_located(locator))
    element.click()

def send_data(data,locator):
    element = wait.until(expected_conditions.visibility_of_element_located(locator))
    element.send_keys(data)

def get_text(locator):
    element = wait.until(expected_conditions.visibility_of_element_located(locator))
    return element.text


