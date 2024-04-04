import time

from selenium import webdriver
from selenium.webdriver.common.by import By

URL = "https://automationbysqatools.blogspot.com/2021/05/dummy-website.html"

driver = webdriver.Chrome()
driver.implicitly_wait(10)
driver.maximize_window()
driver.get(URL)

#### Get title of the website

title = driver.title
print("Title of the page:",title)

#### Get list of elements

web_elements = driver.find_elements(By.XPATH,"//input[@type='checkbox']")

for element in web_elements:
    enabled = element.is_enabled()
    print("Enabled :", enabled)

    displayed = element.is_displayed()
    print("Displayed:",displayed)

    selected = element.is_selected()
    print("Selected:",selected)                     # False bcoz not selected yet , not clicked
    element.click()

    print("Check is selected:",selected)            # True , its clicked now
    print("__"*60)

time.sleep(5)
driver.close()
