import time
from selenium import  webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

driver = webdriver.Chrome()
wait = WebDriverWait(driver, 15, poll_frequency=1)
driver.maximize_window()
driver.get("https://automationbysqatools.blogspot.com/p/manual-testing.html")

element = wait.until(ec.visibility_of_element_located((By.LINK_TEXT, "Software Testing Principles")))
element.click()
time.sleep(5)

driver.close()