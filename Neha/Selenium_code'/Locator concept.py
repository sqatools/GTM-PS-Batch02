"""
ID # Done
XPATH
LINK_TEXT # Done
PARTIAL_LINK_TEXT # Done
NAME  # Done
TAG_NAME # DONE   # IT slight difficult to find unique tag name on the webpage
CLASS_NAME # Done
CSS_SELECTOR
"""

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(10)
driver.get("https://automationbysqatools.blogspot.com/2021/05/dummy-website.html")
driver.implicitly_wait(3)
#Class
Validating_class = driver.find_element(By.CLASS_NAME,"post-title").text
print(f"Class element text: {Validating_class}")
driver.implicitly_wait(3)
#Tag name
Validating_Tag = driver.find_element(By.TAG_NAME,'h1').text
print(f"Tag element text:{Validating_Tag}")
driver.implicitly_wait(3)
#ID
driver.find_element(By.ID,"firstname").send_keys("Neha")
driver.implicitly_wait(3)
#Name
driver.find_element(By.NAME,"fromcity").send_keys("Delhi")
driver.find_element(By.NAME,'destcity').send_keys("Bengalore")
driver.implicitly_wait(3)
#Link text
driver.find_element(By.LINK_TEXT,"Manual Testing").click()
driver.implicitly_wait(3)
#Partial Link text
driver.find_element(By.PARTIAL_LINK_TEXT,"Monkey").click()
driver.implicitly_wait(3)
driver.close()


