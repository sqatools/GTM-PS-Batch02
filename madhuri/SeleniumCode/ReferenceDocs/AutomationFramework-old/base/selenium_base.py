from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


class SeleniumBase:
    def __init__(self, driver, timeout=30):
        self.driver = driver
        self.timeout = timeout
        self.wait = WebDriverWait(self.driver, timeout=self.timeout)

    def get_element(self, locator):
        try:
            element = self.wait.until(ec.visibility_of_element_located(locator))
            return element
        except Exception as e:
            print(e)
            print(f"Element not found, {locator}")

    def click_element(self, locator):
        element = self.get_element(locator)
        if element:
            element.click()
        else:
            print("Element not found")

    def enter_value(self, locator, data):
        element = self.get_element(locator)
        if element:
            element.send_keys(data)
        else:
            print("Element not found")
