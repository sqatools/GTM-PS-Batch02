import time

from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec

driver = webdriver.Chrome()
wait = WebDriverWait(driver,15,0.5)
driver.get("https://automationbysqatools.blogspot.com/p/manual-testing.html")
driver.maximize_window()

element_1=wait.until(ec.visibility_of_element_located((By.LINK_TEXT,"What is Software Testing")))
element_1.click()
time.sleep(10)
element_2=wait.until(ec.visibility_of_element_located((By.LINK_TEXT,"What is Manual Testing")))
element_2.click()
time.sleep(10)

element_3=wait.until(ec.visibility_of_element_located((By.LINK_TEXT,"Software Testing Principles")))
element_3.click()
time.sleep(10)

window_list = driver.window_handles
print(window_list)

driver.switch_to.window(window_list[2])
time.sleep(3)

driver.switch_to.window(window_list[1])
time.sleep(3)

driver.switch_to.window(window_list[0])
search=wait.until(ec.visibility_of_element_located((By.NAME,"q")))
search.send_keys("selenium")
time.sleep(10)




