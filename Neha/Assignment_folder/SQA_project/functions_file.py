from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.select import Select



web_URL = "https://automationbysqatools.blogspot.com/2021/05/dummy-website.html"
wait = None
def get_driver(web_URL , Browser , timeout):
    if Browser.lower() == 'chrome':
        driver = webdriver.Chrome()
    elif Browser.lower() == 'firefox':
        driver = webdriver.Firefox()
    global wait
    wait = WebDriverWait(driver,timeout, poll_frequency=0.5)
    driver.maximize_window()
    driver.get(web_URL)

def get_element(locator):
    try:
        element = wait.until(ec.visibility_of_element_located(locator))
        return element
    except Exception as e:
        print(e)
        print(f"Unable to find element with the locator: {locator}")
        driver.save_screenshot("element_not_found.png")

def get_elements(locator):
    try:
        elements = wait.until(ec.visibility_of_element_located(locator))
        return elements
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

def click_elements(locator):
    elements = get_elements(locator)
    if elements is not None:
        elements.click()
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
        # select_obj.select_by_visible_text(value)
        select_obj.select_by_value(value)
    else:
        print(f"No element found :{locator}")

def click_radio_option(locator):
    elements = wait.until(ec.visibility_of_all_elements_located(locator))
    for element in elements:
        radio_value = element.get_attribute("value")
        if radio_value == 'radio_123':
            element.click()
            print("is selected: ", element.is_selected())
            break



"""
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
        
def click_radio_option(locator):
    elements = wait.until(ec.visibility_of_all_elements_located(locator))
    for element in elements:
        radio_value = element.get_attribute("value")
        if radio_value == 'radio_123':
            element.click()
            print("is selected: ", element.is_selected())
            break

"""




