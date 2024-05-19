import time
from selenium import webdriver
from selenium.webdriver.common.by import By

URL="https://automationbysqatools.blogspot.com/2021/05/dummy-website.html"

driver=webdriver.Chrome()
driver.maximize_window()
driver.get(URL)
driver.find_element(By.XPATH,"//input[@type='checkbox']").click()
time.sleep(10)