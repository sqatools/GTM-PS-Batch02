import time

from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec

driver=webdriver.Chrome()
wait=WebDriverWait(driver,15,0.5)
driver.get("https://automationbysqatools.blogspot.com/p/manual-testing.html")
driver.maximize_window()
time.sleep(5)

Tab2=wait.until(ec.visibility_of_element_located((By.LINK_TEXT,"What is Manual Testing")))
Tab2.click()
time.sleep(5)

window_element=driver.window_handles
print(window_element)

driver.switch_to.window(window_element[0])
search_element=wait.until(ec.visibility_of_element_located((By.NAME,"q")))
search_element.send_keys("selenium")
time.sleep(5)
driver.close()

driver.switch_to.window(window_element[1])
Home_element=wait.until(ec.visibility_of_element_located((By.LINK_TEXT,"Home")))
Home_element.click()
time.sleep(5)


