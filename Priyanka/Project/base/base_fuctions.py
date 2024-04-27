from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.select import Select
from pytest_html_reporter import attach
from utilities.get_logger import logger
from utilities.utils import *

log = logger

class SeleniumBase:
    def __init__(self, driver, timeout=30):
        self.driver = driver
        self.timeout = timeout
        self.wait = WebDriverWait(self.driver, timeout=self.timeout)
