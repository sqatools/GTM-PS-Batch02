from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
driver.maximize_window()
driver.implicitly_wait(10)
driver.find_element(By.NAME ,"username").send_keys("Admin")
driver.implicitly_wait(10)
driver.find_element(By.NAME, "password").send_keys("admin123")
driver.implicitly_wait(10)
driver.find_element(By.XPATH , '//button[@type="submit"]').click()
driver.implicitly_wait(10)
driver.close()
