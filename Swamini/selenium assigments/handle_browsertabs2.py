import time

from selenium import  webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.alert import Alert

driver = webdriver.Chrome()
wait = WebDriverWait(driver, 15, poll_frequency=1)
driver.maximize_window()
driver.get("https://automationbysqatools.blogspot.com/p/manual-testing.html")

element = wait.until(ec.visibility_of_element_located((By.LINK_TEXT, "Software Testing Principles")))
element.click() #1
time.sleep(2)

bb_element = wait.until(ec.visibility_of_element_located((By.LINK_TEXT, "Black Box Testing")))
bb_element.click() #2
time.sleep(3)

bb_element = wait.until(ec.visibility_of_element_located((By.LINK_TEXT, "White Box Testing")))
bb_element.click() #3
time.sleep(4)

windows_list = driver.window_handles
print(windows_list)

driver.switch_to.window(windows_list[3])
search_element3 = wait.until(ec.visibility_of_element_located((By.NAME, "q")))
search_element3.send_keys("Screen3")
time.sleep(5)

driver.switch_to.window(windows_list[2])
search_element2 = wait.until(ec.visibility_of_element_located((By.NAME, "q")))
search_element2.send_keys("Screen2")
time.sleep(5)
driver.switch_to.window(windows_list[1])
search_element1 = wait.until(ec.visibility_of_element_located((By.NAME, "q")))
search_element1.send_keys("Screen1")
time.sleep(5)
driver.switch_to.window(windows_list[0])
search_element = wait.until(ec.visibility_of_element_located((By.NAME, "q")))
search_element.send_keys("Screen0")
time.sleep(5)
home_element = wait.until(ec.visibility_of_element_located((By.XPATH, "//li/a[text()='Home']")))
home_element.click()
time.sleep(5)

driver.close()











