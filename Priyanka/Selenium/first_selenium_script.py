import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://www.google.co.in")
driver.maximize_window()
driver.implicitly_wait(10)
driver.find_element(By.NAME, "q").send_keys("Python selenium")
driver.find_element(By.NAME, "btnk").click()
time.sleep(10)
driver.close()
