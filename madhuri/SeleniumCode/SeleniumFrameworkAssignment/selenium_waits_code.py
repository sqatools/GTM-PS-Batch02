import time
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.select import Select

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


def get_element(locator):
    element = wait.until(ec.visibility_of_element_located(locator))
    return element


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


def select_radio_option(value, locator):
    elements = wait.until(ec.visibility_of_all_elements_located(locator))
    for element in elements:
        radio_value = element.get_attribute("value")
        if radio_value == value:
            element.click()
            print("is selected: ", element.is_selected())
            break


def select_checkboxes(values, locator):
    elements = wait.until(ec.visibility_of_all_elements_located(locator))
    print(values)
    for element in elements:
        checkbox_value = element.get_attribute("value")
        print('checkbox value: ', checkbox_value)

def click_citi_options(locator):
    elements = wait.until(ec.visibility_of_all_elements_located(locator))
    i = 1
    for element in elements:
        checkbox_value = element.get_attribute("value")
        if i == 2:
            element.click()
            break

        i = i + 1


def select_dropdown_by_value(value, locator):
    element = get_element(locator)
    select_obj = Select(element)
    select_obj.select_by_value(value)


def select_dropdown_by_visible_text(value, locator):
    element = get_element(locator)
    select_obj = Select(element)
    select_obj.select_by_visible_text(value)
