"""
ID # Done
XPATH #
LINK_TEXT # Done
PARTIAL_LINK_TEXT # Done
NAME  # Done
TAG_NAME # DONE   # IT slight difficult to find unique tag name on the webpage
CLASS_NAME # Done
CSS_SELECTOR
"""
import time

from selenium import webdriver
from selenium.webdriver.common.by import By


driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(10)
driver.get("https://automationbysqatools.blogspot.com/2021/05/dummy-website.html")

from_city = driver.execute_script("return document.getElementById('fromcity')")

from_city.send_keys("Mumbai")
time.sleep(10)

current_url = driver.execute_script("return document.URL")
website_title = driver.execute_script("return document.title")
print("Website URL :", current_url)
print("website_title :", website_title)

driver.execute_script("window.open('https://www.google.co.in', '_blank')")
time.sleep(10)

driver.close()
