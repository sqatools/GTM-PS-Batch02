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

    def get_elements(self, locator):
        try:
            elements = self.wait.until(ec.visibility_of_all_elements_located(locator))
            return elements
        except Exception as e:
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

    def clear_input(self, locator):
        element = self.get_element(locator)
        element.clear()


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

    def rate_by_star(self, locator, label, count):
        elements = self.get_elements(locator)
        print(elements)
        for element in elements:
            print("before count: ", count)
            if count > 0:
                element.click()
            count = count - 1
            print("after count: ", count)
        return element



