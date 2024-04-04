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

Actual_title = driver.title
driver.implicitly_wait(3)
Expected_title = "OrangeHRM"

if Actual_title == Expected_title:
    print(f"Logged In successfully")
else:
    print("logged In unsuccessfull")

##Admin Tab

driver.find_element(By.XPATH, "//button[@type ='button']").click()
driver.implicitly_wait(3)
driver.find_element(By.XPATH,"//span[contains(text(),'/Admin']").click()
page_title = driver.find_element(By.TAG_NAME,"User Management").click()
##Fields
search = driver.find_element(By.XPATH,"//button[@type = 'submit']")
driver.implicitly_wait(3)
search.click()
driver.close()
