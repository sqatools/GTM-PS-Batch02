import time

from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.select import Select

"""
implicit wait : This wait will apply on all the web element of the website.
explicit wait : explicit wait will apply on specific element with given condition.
static wait : time.sleep(10) , User has to wait till specified time to move ahead.
"""
website_url = "https://automationbysqatools.blogspot.com/2021/05/dummy-website.html"
wait = None
driver = None


def get_driver(URL, BROWSER, timeout):
    global driver
    if BROWSER.lower() == 'chrome':
        driver = webdriver.Chrome()
    elif BROWSER.lower() == 'firefox':
        driver = webdriver.Firefox()
    global wait
    wait = WebDriverWait(driver, timeout, poll_frequency=0.5)
    driver.maximize_window()
    # driver.implicitly_wait(10)
    driver.get(URL)
    # return driver, wait


def get_element(locator):
    try:
        element = wait.until(ec.visibility_of_element_located(locator))
        return element
    except Exception as e:
        print(e)
        print(f"Unable to find element with the locator: {locator}")
        driver.save_screenshot("element_not_found.png")


def click_element(locator):
    element = get_element(locator)
    if element is not None:
        element.click()
    else:
        print(f"No element found :{locator}")


def send_data(data, locator):
    element = get_element(locator)
    if element is not None:
        element.send_keys(data)
    else:
        print(f"No element found:{locator}")


def get_text(locator):
    element = get_element(locator)
    if element is not None:
        return element.text
    else:
        print(f"No element found :{locator}")


def select_dropdown_value(locator, value):
    element = get_element(locator)
    if element is not None:
        select_obj = Select(element)
        select_obj.select_by_visible_text(value)
    else:
        print(f"No element found :{locator}")
