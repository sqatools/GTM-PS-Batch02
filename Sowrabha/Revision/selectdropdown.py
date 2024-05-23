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
time.sleep(10)
