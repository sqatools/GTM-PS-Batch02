import time

from selenium import webdriver
from selenium.webdriver.common.by import By
#from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

"""
implicit wait : This wait will apply on all the web element of the website.
explicit wait : explicit wait will apply on specific element with given condition.
static wait : time.sleep(10) , User has to wait till specified time to move ahead.
"""

URL = "https://automationbysqatools.blogspot.com/2021/05/dummy-website.html"


driver = webdriver.Chrome()
wait = WebDriverWait(driver, 15, poll_frequency=0.5)
driver.maximize_window()
driver.implicitly_wait(10)
driver.get(URL)

# get title of the website
title = driver.title
print("Website title :", title)
try:
    t1 = time.time()
    driver.find_element(By.ID, "street_address3").send_keys("Mumbai Boriwali")
except Exception as e:
    print(e)
t2 = time.time()
print("total time taken :", t2-t1)

ta = time.time()
try:
    element = wait.until(ec.visibility_of_element_located((By.ID, "billing_email1")))
    print(element)
    element.send_keys("admin@gmail.com")
except Exception as e:
    print(e)
tb = time.time()
print("total time taken email field :", tb-ta)

time.sleep(5)
driver.close()
