"""
implicit wait : This wait will apply on all the web elements of the website, globally for entire code, general wait
                Global wait
                It is not consuming entire time 10s , if it identifies in 1s then it will continue rest of the code
                Do not waste the time
                default time is less than 1s

explicit wait : Dynamic Wait, Specific wait , WebDriverWait, Conditional Wait
                Apply on specific element with given condition

Fluent Wait : Frequency it polls in the DOM
               timeout: float,
                poll_frequency: float = POLL_FREQUENCY,
                 ignored_exceptions: typing.Optional[WaitExcTypes] = None,

static wait :  Python wait not Selenium wait
               time.sleep(10)
               User has to wait till the specified time to move ahead

"""

import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

URL = "https://automationbysqatools.blogspot.com/2021/05/dummy-website.html"

driver = webdriver.Chrome()
wait = WebDriverWait(driver,15,poll_frequency=0.5)

driver.implicitly_wait(10)
driver.maximize_window()
driver.get(URL)                                 # Not wait for page to get loaded

try:
  t1 = time.time()
  driver.find_element(By.ID,"street_address3").send_keys("Scotland")         # street_address3 If wrong ID is given then exception
  # no such element: Unable to locate element: {"method":"css selector","selector":"[id="street_address3"]"}
  # street_address1
except Exception as e:
    print(e)
t2 = time.time()                                                                # try and except block

print("Total time taken:",t2-t1)                                               # Total time taken: 0.058747291564941406

ta= time.time()

try:
      element = wait.until(expected_conditions.visibility_of_element_located((By.ID,"billing_email")))        # email address # billing_email
      # billing_email1 wrong ID so use try and except to handle the exception of wrong ID
      print(element)
      print(element.send_keys("admin@gmail.com"))
except Exception as e:
      print(e)
tb = time.time()
print("Total time:", tb-ta)

driver.close()