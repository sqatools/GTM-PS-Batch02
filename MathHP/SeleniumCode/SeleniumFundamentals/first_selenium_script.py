import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()                   # Launch empty browser
# driver=webdriver.Firefox()
# driver=webdriver.Edge()                    # Multi browser launching

driver.get("https://www.google.co.in/")
driver.find_element(By.ID,"L2AGLb").click()           # accept cookies

driver.maximize_window()
driver.implicitly_wait(10)

driver.find_element(By.ID,"APjFqb").send_keys("Python Selenium")        # search
time.sleep(5)

driver.find_element(By.NAME,"btnK").click()                               # google search
time.sleep(10)

#driver.close()


