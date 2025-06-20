import time

from selenium import  webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.action_chains import ActionChains
driver = webdriver.Chrome()
driver.get("https://www.globalsqa.com/demo-site/frames-and-windows/#iFrame")
wait = WebDriverWait(driver, 15)

def move_to_element(element):
    action = ActionChains(driver)
    action.move_to_element(element)
    action.perform()

def click_to_element(element):
    action = ActionChains(driver)
    action.click(element)
    action.perform()

element_menu = wait.until(ec.visibility_of_element_located((By.XPATH, "//div[@id='menu']//a[text()='Tester’s Hub']")))
move_to_element(element_menu)

demo_testing = wait.until(ec.visibility_of_element_located((By.XPATH, "//*[contains(text(),'Demo Testing Site')]")))
move_to_element(demo_testing)
time.sleep(5)

tool_tip = wait.until(ec.visibility_of_element_located((By.XPATH, "//*[contains(text(),'Tooltip')]")))
click_to_element(tool_tip)

time.sleep(5)

driver.close()
