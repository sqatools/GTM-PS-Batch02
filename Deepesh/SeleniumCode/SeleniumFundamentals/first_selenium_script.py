"""import time
from selenium import webdriver
from selenium.webdriver.common.by import By

#from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
#driver = webdriver.Firefox()
#driver = webdriver.Edge()
driver.get("https://www.google.co.in")
driver.maximize_window()
driver.implicitly_wait(10)
driver.find_element(By.NAME, "q").send_keys("Python Selenium")
driver.find_element(By.NAME, "btnK").click()
time.sleep(5)
driver.close()"""


import time
from selenium import webdriver
from selenium.webdriver.common.by import By


driver = webdriver.Chrome()

driver.get("https://automationbysqatools.blogspot.com/2021/05/dummy-website.html")
driver.maximize_window()
driver.implicitly_wait(10)

driver.find_element(By.XPATH, "//div[@id='billing_details']//following-sibling::input[@ type='checkbox']").click()

time.sleep(5)
driver.close()