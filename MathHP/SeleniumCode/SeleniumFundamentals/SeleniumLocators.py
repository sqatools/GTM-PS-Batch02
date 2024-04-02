"""
8 LOCATORS

ID                                # Usually unique , Every webelement has unique id
NAME
TAG NAME                          # slightly difficult to find unique tagname in webpage
CLASS

LINK TEXT
PARTIAL LINKED TEXT

XPATH
CSS

"""
import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(10)
driver.get("https://automationbysqatools.blogspot.com/2021/05/dummy-website.html")
#driver.close()         without close() method also browser automatically closes

got_it_cookies_accept = driver.find_element(By.ID,"cookieChoiceDismiss").click()

# Class name:

dummy_sub_heading = driver.find_element(By.CLASS_NAME,"post-title").text
print("Sub heading text:",dummy_sub_heading)                                                         # Sub heading text: Dummy Website

# Tag name:

expected_text = "Dummy Ticket Booking Website"
dummy_ticket_booking_website = driver.find_element(By.TAG_NAME,"h1")
actual_text = dummy_ticket_booking_website.text
print("Expected:" ,expected_text)                                                               # Expected: Dummy Ticket Booking Website
print("Actual:",actual_text)                                                                   # Actual: Dummy Ticket Booking Website
assert expected_text == actual_text

#ID

from_city_textbox =driver.find_element(By.ID,"fromcity").send_keys("Mumbai")                              # From City
time.sleep(5)

# Name

to_city_textbox= driver.find_element(By.NAME,"destcity").send_keys("Chennai")

# Link text

time.sleep(5)

code_practice_link = driver.find_element(By.LINK_TEXT,"Code Practice").click()                      #ElementClickInterceptedException

time.sleep(5)

# Partial Link text

python_basic_programs_link = driver.find_element(By.PARTIAL_LINK_TEXT,"Python Basic ").click()

driver.close()






