from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

class selenium_base:
    def __init__(self,driver,timeout=30):
        self.driver=driver
        self.timeout=timeout
        self.wait=WebDriverWait(self.driver,timeout=self.timeout)

    def get_elemtnt(self,locator):
        try:
            element=self.wait.until(ec.visibility_of_element_located(locator))
            return element
