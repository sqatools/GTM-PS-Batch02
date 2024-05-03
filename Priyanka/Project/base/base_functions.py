from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.select import Select
#from pytest_html_reporter import attach
from utilities.get_logger import logger
from utilities.utils import *

log = logger

class SeleniumBase:
    def __init__(self, driver, timeout=30):
        self.driver = driver
        self.timeout = timeout
        self.wait = WebDriverWait(self.driver, timeout=self.timeout)

    def navigate_to_url(self, URL):
        self.driver.get(URL)

    def get_element(self, locator):
        try:
            element = self.wait.until(ec.visibility_of_element_located(locator))
            return element
        except Exception as e:
            log.info(e)
            log.info(f"element not found {locator}")
            raise

    def click_element(self, locator):
        try:
            element = self.get_element(locator)
            log.info(f"Got element with the locator : {locator}")
            if element:
                element.click()
            else:
                log.info(f"element not found {locator}")
        except Exception as e:
            log.info(e)


    def enter_value(self, locator, value):
        element = self.get_element(locator)
        if element:
            element.send_keys(value)
        else:
            log.info(f"element not found {locator}")

    def get_text(self, locator):
        element = self.get_element(locator)
        if element:
            return element.text
        else:
            log.info(f"element not found {locator}")

    def select_value_from_dropdown(self, locator, value):
        element = self.get_element(locator)
        if element:
            obj = Select(element)
            obj.select_by_visible_text(value)
        else:
            log.info(f"element not found {locator}")

    def get_attribute(self, locator, attribute_name):
        element = self.get_element(locator)
        log.info(f"Got element with the locator : {locator}")
        if element:
            return element.get_attribute(attribute_name)
        else:
            log.error("Element not found")

    def windows_handle(self):
        window_list = self.driver.window_handles
        return self.driver.switch_to.window(window_list[1])

    def get_elements(self, locator):
        web_elements = self.driver.find_elements(locator)
        return web_elements

    def switch_to_default_windows(self):
        window_list = self.driver.window_handles
        self.driver.close()
        return self.driver.switch_to.window(window_list[0])


