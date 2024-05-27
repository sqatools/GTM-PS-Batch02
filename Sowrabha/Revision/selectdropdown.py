from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.select import Select
import time

URL="https://automationbysqatools.blogspot.com/2021/05/dummy-website.html"
driver=webdriver.Chrome()
Wait=WebDriverWait(driver,15)
driver.maximize_window()
driver.get(URL)
element=Wait.until(ec.visibility_of_element_located((By.ID,"billing_country")))
Select.obj=Select(element)
Select.obj.select_by_visible_text("Bangladesh")
time.sleep(4)

#Date field

dept_date=Wait.until(ec.visibility_of_element_located((By.ID,"departdate")))
dept_date.send_keys("10/10/2024")
time.sleep(5)
dept_date.screenshot("deptscreenshot.png")

#radio button
driver.find_element(By.XPATH,"//input[@value='radio_123']").click()
driver.save_screenshot("webpage.png")
time.sleep(5)

#Get attribute value
radio_element=Wait.until(ec.visibility_of_element_located((By.XPATH,"//input[@type='radio']")))
attribute_value=radio_element.get_attribute("value")
print("attribute value is",attribute_value)
time.sleep(10)