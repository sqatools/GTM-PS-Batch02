import time

from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as ec

driver=webdriver.Chrome()
wait=WebDriverWait(driver,15,0.5)
driver.get("https://www.globalsqa.com/demo-site/frames-and-windows")
driver.maximize_window()

def move_to_element(element):
   Action =ActionChains(driver)
   Action.move_to_element(element)
   Action.perform()

def click_to_element(element):
   Action=ActionChains(driver)
   Action.click(element)
   Action.perform()

element1=wait.until(ec.visibility_of_element_located((By.XPATH,"//div[@id='menu']//a[text()='Tester’s Hub']")))
move_to_element(element1)

element2=wait.until(ec.visibility_of_element_located((By.XPATH,"//*[contains(text(),'Demo Testing Site')]")))
move_to_element(element2)

element3=wait.until(ec.visibility_of_element_located((By.XPATH,"//*[contains(text(),'Tooltip')]")))
click_to_element(element3)

time.sleep(10)