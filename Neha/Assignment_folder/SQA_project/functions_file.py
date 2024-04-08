from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


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
    element = wait.until(ec.visibility_of_element_located(locator))
    return element

def click_element(locator):
    element = get_element(locator)
    element.click()

def send_data(data , locator):
    element = get_element(locator)
    element.send_keys(data)

def get_text(locator):
    element = get_element(locator)
    return element.text

