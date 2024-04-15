import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.alert import Alert

driver = webdriver.Chrome()
wait = WebDriverWait(driver, timeout=15, poll_frequency= 1)
driver.maximize_window()
driver.get("https://automationbysqatools.blogspot.com/2020/08/alerts.html")

# Alert Box
element = wait.until(ec.visibility_of_element_located((By.ID, "btnShowMsg")))
element.click()
time.sleep(3)

alert_obj = Alert(driver)
print("Alert Message: ", alert_obj.text)
alert_obj.accept()


# Javascript Confirm Box
element2 = wait.until(ec.visibility_of_element_located((By.XPATH, "//h2[contains(text(),'JavaScript Confirm Box')]//following::button[1]")))
element2.click()
time.sleep(3)
alert_obj2 = Alert(driver)
# alert_obj2.accept()
alert_obj2.dismiss()

element3 = wait.until(ec.visibility_of_element_located((By.ID, "demo")))
print("Javascript Click Button Text: ", element3.text)

#JavaScript Prompt Box
element4 = wait.until(ec.visibility_of_element_located((By.ID, "promptbtn")))
element4.click()
time.sleep(3)

alert_obj3 = Alert(driver)
print("Javascript Prompt Box: ", alert_obj3.text)
# alert_obj3.clear()
alert_obj3.send_keys("GTM Training")
alert_obj3.accept()

element5 = wait.until(ec.visibility_of_element_located((By.ID, "prompt")))
print("Javascript Prompt Box Text: ", element5.text)
driver.save_screenshot("alert_page.png")
element5.screenshot("prompt_box.png")
time.sleep(5)

