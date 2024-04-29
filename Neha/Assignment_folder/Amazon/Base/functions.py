from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.action_chains import ActionChains


class AmazonBase:
    def __init__(self,driver,timeout =20):
        self.driver = driver
        self.timeout = timeout
        self.wait = WebDriverWait.until(self.driver , timeout= self.timeout)

    def get_element(self,locator):
        try:
            element = self.wait.until(ec.visibility_of_element_located(locator))
            return element
        except Exception as e:
        print(e)
        print(f"Element not found, {locator}")

    def click_element(self,locator):
        element = self.get_element(locator)
        if element:
            element.click()
        else:
            print(f"element Not found exception:{locator}")

    def enter_values(self,locator,data):
        element = self.get_element(locator)
        if element:
            element.sendkeys(data)
        else:
            print(f"element Not found exception:{locator}")

    def mousehover_click_to_element(self,locator):
        element = self.get_element(locator)
        action = ActionChains(self.driver)
        action.click(element)
        action.perform()

    def mousehover_move_to_element(self,locator):
        element = self.get_element(locator)
        action = ActionChains(self.driver)
        action.move_to_element(element)
        action.perform()



