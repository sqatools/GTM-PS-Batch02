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
#
# #def click_element(locator):
#     element=Wait.until(ec.visibility_of_element_located(locator))
#     element.click()
#
# #def send_data(data,locator):
#     element=Wait.until(ec.visibility_of_element_located(locator))
#     element.send_keys(data)

def get_element(locator):
    try:
        element = Wait.until(ec.visibility_of_element_located(locator))
        return element
    except Exception as e:
        print(e)
        print(f"unable to find the element with the locator:{locator}")

def click_element(locator):
    element=get_element(locator)
    if element is not None:
       element.click()
    else:
        print("element not found")

def send_keys(data,locator):
    element=get_element(locator)
    if element is not None:
       element.send_keys(data)
    else:
        print("element not found")

def get_text(locator):
    element=get_element(locator)
    if element is not None:
        return element.text
    else:
        print("element not found")


# def get_element(locator):
#     try:
#         element = Wait.until(ec.visibility_of_element_located(locator))
#         return element
#     except Exception as e:
#         print(e)
#         print(f"Unable to find the element with the locator: {locator}")
#
# def click_element(locator):
#     element = get_element(locator)
#     if element is not None:
#        element.click()
#     else:
#         print("Element not found")
#
# def send_keys(data, locator):
#     element = get_element(locator)
#     if element is not None:
#        element.send_keys(data)
#     else:
#         print("Element not found")
#
# def get_text(locator):
#     element = get_element(locator)
#     if element is not None:
#        return element.text
#     else:
#         print("Element not found")
#         return None