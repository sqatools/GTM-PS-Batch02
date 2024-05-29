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
element=wait.until(ec.visibility_of_element_located((By.ID,"button")))
element.click()
alert_obj=Alert(driver)
print("alert message",alert_obj.text)
alert_obj.dismiss()
ui_element=wait.until(ec.visibility_of_element_located((By.ID,"demo")))
print("ui MESSAGE:",ui_element.text)
time.sleep(10)
