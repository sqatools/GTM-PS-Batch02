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
import time

from selenium import webdriver
from selenium.webdriver.common.by import By


driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(10)
driver.get("https://automationbysqatools.blogspot.com/2021/05/dummy-website.html")

# CLASS NAME :
dummy_sub_heading = driver.find_element(By.CLASS_NAME, "post-title").text
print("Sub heading text :", dummy_sub_heading)

# TAGNAME
expected_header_Text = "Dummy Ticket Booking Website"
header_text = driver.find_element(By.TAG_NAME, "h1").text
print("header text value :", header_text)
assert expected_header_Text == header_text

# ID Locator
# Every web element should have unique ID attribute, if there is no unique id, then we can
# use it
driver.find_element(By.ID, "fromcity").send_keys("Mumbai")

# NAME Locator:
driver.find_element(By.NAME, "destcity").send_keys("Bangalore")

# LINK TEXT
driver.find_element(By.LINK_TEXT, "Code Practice").click()
time.sleep(2)

# PARTIAL LINK TEXT
driver.find_element(By.PARTIAL_LINK_TEXT, "Python Basic").click()

time.sleep(5)
driver.close()

