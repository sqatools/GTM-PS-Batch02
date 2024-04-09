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

driver = webdriver.Chrome()                        # Launch empty Chrome browser
driver.implicitly_wait(10)
driver.maximize_window()
driver.get("https://www.booking.com/index.en-gb.html?label=gen173nr-1BCAEoggI46AdIM1gEaFCIAQGYAQm4ARfIAQzYAQHoAQGIAgGoAgO4Av2CtrAGwAIB0gIkMTMyZWZmNGMtYTQ2YS00YTc4LWIzNzAtMzMzYTBjZDFiMzNm2AIF4AIB&sid=68ffc143cb30c44d2c8c652c14b07e2f&keep_landing=1&sb_price_type=total&")

cookies_accept = driver.find_element(By.ID,"onetrust-accept-btn-handler")
cookies_accept.click()

Where_are_you_going_textbox = driver.find_element(By.XPATH,"//input[@placeholder='Where are you going?']")
Where_are_you_going_textbox.send_keys("Manchester, United Kingdom")

time.sleep(4)
driver.close()


