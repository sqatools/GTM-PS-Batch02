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
driver.get("https://www.booking.com/")

driver.find_element(By.XPATH, "//input[@placeholder='Where are you going?']").send_keys("Goa")

time.sleep(5)
driver.close()
