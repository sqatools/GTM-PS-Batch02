import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

driver=webdriver.Chrome()
wait=WebDriverWait(driver,15,0.5)
driver.get("https://www.globalsqa.com/demo-site/frames-and-windows")
driver.maximize_window()

iframe_element=wait.until(ec.visibility_of_element_located((By.ID,"iFrame")))
iframe_element.click()
time.sleep(6)

driver.switch_to.frame(iframe_element)
search_element=wait.until(ec.visibility_of_element_located((By.ID,"s")))
search_element.send_keys("selenium")
search_element.click()
time.sleep(5)
