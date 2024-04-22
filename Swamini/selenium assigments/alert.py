import time

from selenium import  webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.alert import Alert

driver = webdriver.Chrome()
wait = WebDriverWait(driver, 15, poll_frequency=1)
driver.maximize_window()
driver.get("https://automationbysqatools.blogspot.com/2020/08/alerts.html")


# Alert Box
element = wait.until(ec.visibility_of_element_located((By.ID, "btnShowMsg")))
element.click()
time.sleep(5)
alert_obj = Alert(driver)
print("alert msg :", alert_obj.text)
alert_obj.accept()


# Confirm Box
"""
element = wait.until(ec.visibility_of_element_located((By.ID, "button")))
element.click()
time.sleep(5)
alert_obj = Alert(driver)
print("alert msg :", alert_obj.text)
#alert_obj.accept()
alert_obj.dismiss()
ui_msg_elem = wait.until(ec.visibility_of_element_located((By.ID, "demo")))
print("Text Msg on UI:", ui_msg_elem.text)
"""

# Prompt Box
# element = wait.until(ec.visibility_of_element_located((By.ID, "promptbtn")))
# element.click()
# time.sleep(5)
# alert_obj = Alert(driver)
# print("alert msg :", alert_obj.text)
# alert_obj.send_keys("GTM Training")
# alert_obj.accept()
# #alert_obj.dismiss()
# ui_msg_elem = wait.until(ec.visibility_of_element_located((By.ID, "prompt")))
# print("Text Msg on UI:", ui_msg_elem.text)

driver.save_screenshot("E:\\log\\alert_page.png")


time.sleep(5)

driver.close()



