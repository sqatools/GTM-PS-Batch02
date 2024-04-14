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
element.click()

windows_list = driver.window_handles
print(windows_list)

driver.switch_to.window(windows_list[1])
header_xpath = "//h3[contains(text(), 'Software Testing Principles')]"
header = wait.until(ec.visibility_of_element_located((By.XPATH, header_xpath)))
assert header.text == 'Software Testing Principles'

search_element = wait.until(ec.visibility_of_element_located((By.NAME, "q")))
search_element.send_keys("Selenium")
time.sleep(5)

driver.close()

driver.switch_to.window(windows_list[0])
driver.refresh()
# driver.back()
# driver.forward()

home_element = wait.until(ec.visibility_of_element_located((By.XPATH, "//li/a[text()='Home']")))
home_element.click()

time.sleep(5)

driver.close()











