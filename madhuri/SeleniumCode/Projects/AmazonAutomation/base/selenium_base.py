from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.select import Select
from utilities.get_logger import logger
from utilities.utils import *
log = logger


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
            log.info(f"{e}")
            log.error(f"Element not found, {locator}")
            filename = get_unique_name()
            self.driver.save_screenshot(f"/logs/{filename}.png")
            raise

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
        try:
            element = self.get_element(locator)
            return element.text
        except Exception as e:
            log.info(f"{e}")
            log.error(f"Element not found, {locator}")
            raise

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

    def windows_handle(self):
        window_list = self.driver.window_handles
        return self.driver.switch_to.window(window_list[1])

    def switch_to_default_windows(self):
        window_list = self.driver.window_handles
        self.driver.close()
        return self.driver.switch_to.window(window_list[0])

    def select_dropdown(self, locator, value):
        element = self.get_element(locator)
        if element:
            el_obj = Select(element)
            el_obj.select_by_visible_text(value)
        else:
            log.error(f"Element not found", {locator})

