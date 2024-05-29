import time

from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.alert import Alert

driver=webdriver.Chrome()
wait=WebDriverWait(driver,15,0.5)
driver.get("https://automationbysqatools.blogspot.com/2020/08/alerts.html")
driver.maximize_window()
element=wait.until(ec.visibility_of_element_located((By.ID,"btnShowMsg")))
element.click()
time.sleep(5)
alert_obj=Alert(driver)
print("Alert message:",alert_obj.text)
alert_obj.accept()
time.sleep(6)

