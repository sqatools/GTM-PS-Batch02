import time
from selenium import webdriver

from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(10)
driver.get("https://automationbysqatools.blogspot.com/p/home.html")
time.sleep(5)
driver.find_element(By.XPATH,"//div[text()= ' Dummy Website ']"). click()

time.sleep(5)
driver.find_element(By.ID, "fromcity").send_keys("Mumbai")
time.sleep(5)
driver.close()