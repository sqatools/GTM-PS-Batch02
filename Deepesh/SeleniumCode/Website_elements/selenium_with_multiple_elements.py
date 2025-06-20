import time

from selenium import webdriver
from selenium.webdriver.common.by import By

URL = "https://automationbysqatools.blogspot.com/2021/05/dummy-website.html"

driver = webdriver.Chrome()
driver.maximize_window()
driver.get(URL)

# get title of the website
title = driver.title
print("Website title :", title)

# get list of elements
web_elements = driver.find_elements(By.XPATH, "//input[@type='checkbox']")
print(web_elements)
print("Total checkbox :", len(web_elements))
web_elements[2].click()

for element in web_elements:
    print("Check enabled:", element.is_enabled())
    print("Check displayed:", element.is_displayed())
    print("Check is it selected :", element.is_selected())
    element.click()
    print("Check is it selected :", element.is_selected())
    print("_"*50)


time.sleep(5)
driver.close()
