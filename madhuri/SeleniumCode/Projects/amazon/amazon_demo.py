import time

from selenium import  webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.action_chains import ActionChains
driver = webdriver.Chrome()
driver.get("https://www.amazon.in/")
wait = WebDriverWait(driver, 15)

def move_to_element(element):
    action = ActionChains(driver)
    action.move_to_element(element)
    action.perform()

def click_to_element(element):
    action = ActionChains(driver)
    action.click(element)
    action.perform()

# sign_in_register_nav_locator = (By.XPATH, "(//a[@data-nav-ref='nav_ya_signin']//following::span[@class='nav-icon nav-arrow'])[1]")
# register_user_locator =(By.XPATH, "(//div[@id='nav-flyout-accountList']//following::a[contains(text(), 'Start here')])[1]")

element_menu = wait.until(ec.visibility_of_element_located((By.XPATH, "//*[contains(text(),'Account & Lists')]")))
move_to_element(element_menu)
time.sleep(5)

tool_tip = wait.until(ec.visibility_of_element_located((By.XPATH, "(//div[@id='nav-flyout-accountList']//following::a[contains(text(), 'Start here')])[1]")))
click_to_element(tool_tip)

time.sleep(5)
driver.close()
