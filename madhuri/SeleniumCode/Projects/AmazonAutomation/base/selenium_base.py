from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.action_chains import ActionChains

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
            print(f"Element no found, {locator}")

    def enter_values(self, locator, data):
        element = self.get_element(locator)
        if element:
            element.send_keys(data)
        else:
            print(f"Element no found, {locator}")

    def get_text(self, locator):
        element = self.get_element(locator)
        return element.text

    def move_to_element(self, locator):
        element = self.get_element(locator)
        action = ActionChains(self.driver)
        action.move_to_element(element)
        action.perform()

    def click_to_element(self, locator):
        element = self.get_element(locator)
        action = ActionChains(self.driver)
        action.click(element)
        action.perform()




