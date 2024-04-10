import time
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

website_url = "https://automationbysqatools.blogspot.com/2021/05/dummy-website.html"
wait = None


def get_driver(url=website_url, browser='chrome', timeout=15):
    if browser.lower() == 'chrome':
        driver = webdriver.Chrome()
    elif browser.lower() == 'firefox':
        driver = webdriver.Firefox()
    global wait
    wait = WebDriverWait(driver, timeout=15, poll_frequency=0.5)
    driver.maximize_window()
    driver.implicitly_wait(10)
    driver.get(url)
    return driver, wait


def click_element(locator):
    element = wait.until(ec.visibility_of_element_located(locator))
    element.click()
    return element


def send_data(data, locator):
    element = wait.until(ec.visibility_of_element_located(locator))
    element.send_keys(data)


def get_text(locator):
    element = wait.until(ec.visibility_of_element_located(locator))
    return element.text


def click_radio_option(locator):
    elements = wait.until(ec.visibility_of_all_elements_located(locator))
    for element in elements:
        radio_value = element.get_attribute("value")
        if radio_value == 'radio_123':
            element.click()
            print("is selected: ", element.is_selected())
            break

