from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from utilities.get_logger import logger
from pytest_html_reporter import attach
from selenium.webdriver.support.select import Select
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
            log.info(f"Element not found, {locator}")
            attach(data=self.driver.get_screenshot_as_png())
            filename = get_unique_name()
            self.driver.save_screenshot(f"/logs/{filename}.png")
            raise

    def click_element(self, locator):
        element = self.get_element(locator)
        log.info(f"Got element with the locator : {locator}")
        if element:
            element.click()
        else:
            print("Element not found")

    def enter_value(self, locator, data):
        element = self.get_element(locator)
        log.info(f"Got element with the locator:{locator}")
        if element:
            element.send_keys(data)
        else:
            log.error(f"Element not found with the locator:{locator}")

    def get_text(self, locator):
        element = self.get_element(locator)
        log.info(f"Got element with the locator : {locator}")
        if element:
            return element.text
        else:
            log.error("Element not found")

    def select_value_from_dropdown(self, locator, data_select):
        element = self.get_element(locator)
        log.info(f"Got element with the locator : {locator}")
        obj = Select(element)
        if element:
            obj.select_by_visible_text(data_select)
        else:
            print("Element not found")

            return element.text

    def get_attribute(self, locator, attribute_name):
        element = self.get_element(locator)
        log.info(f"Got element with the locator : {locator}")
        if element:
            return element.get_attribute(attribute_name)
        else:
            log.error("Element not found")
