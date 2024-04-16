from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


web_URL ="https://www.amazon.in/"
wait = None
driver = webdriver.Chrome()


def get_driver(web_URL,Browser,timeout):
    if Browser.lower() == 'Chrome':
        driver = webdriver.Chrome()
    elif Browser.lower() == 'Firefox':
        driver = webdriver.Firefox()
    elif Browser.lower() == 'Edge':
        driver = webdriver.Edge()
    global wait
    wait = WebDriverWait( driver , timeout, poll_frequency = 1)
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

def click_element(locator):
    element = get_element(locator)
    if element is not None:
        element.click()
    else:
        print(f"Element not visible:{locator}")

def send_keys(locator,data):
    element = get_element(locator)
    if element is not None:
        element.send_keys(data)
    else:
        print(f"Element not visible:{locator}")

