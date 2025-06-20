import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.action_chains import ActionChains

driver=webdriver.Chrome()
wait=WebDriverWait(driver,15,0.5)
driver.get("https://www.globalsqa.com/demo-site/frames-and-windows")
driver.maximize_window()

element=wait.until(ec.visibility_of_element_located((By.XPATH,"//div[@id='menu']//a[text()='Tester’s Hub']")))
Action= ActionChains(driver)
Action.move_to_element(element)
Action.perform()

time.sleep(10)

element2=wait.until(ec.visibility_of_element_located((By.XPATH,"//*[contains(text(),'Demo Testing Site')]")))
Action.move_to_element(element2)
Action.perform()

time.sleep(10)

element3=wait.until(ec.visibility_of_element_located((By.XPATH,"//*[contains(text(),'Tooltip')]")))
Action.click(element3)
Action.perform()
time.sleep(10)