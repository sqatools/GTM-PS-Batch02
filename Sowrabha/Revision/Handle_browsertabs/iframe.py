import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.alert import Alert

driver=webdriver.Chrome()
wait=WebDriverWait(driver,15,0.5)
driver.get("https://www.globalsqa.com/demo-site/frames-and-windows/#iFrame")
driver.maximize_window()


iframe_element = wait.until(ec.visibility_of_element_located((By.NAME,"globalSqa")))
driver.switch_to.frame(iframe_element)
time.sleep(6)


search_element=wait.until(ec.visibility_of_element_located((By.ID,"s")))
search_element.send_keys("selenium")
search_element.click()
time.sleep(5)
