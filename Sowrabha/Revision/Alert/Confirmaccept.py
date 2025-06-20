import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait


driver=webdriver.Chrome()
wait =WebDriverWait(driver,15,0.5)
driver.get("https://automationbysqatools.blogspot.com/2020/08/alerts.html")
driver.maximize_window()
element=wait.until(ec.visibility_of_element_located((By.ID,"button")))
element.click()
time.sleep(5)
Alert_obj=Alert(driver)
print("alert message:",Alert_obj.text)
Alert_obj.accept()
ui_message=wait.until(ec.visibility_of_element_located((By.ID,"demo")))
print("UI text message",ui_message.text)
time.sleep(10)