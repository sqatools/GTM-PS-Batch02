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
links = ["Software Testing Principles", "Black Box Testing", "White Box Testing"]

temp = 1
for link_text in links:
    element = wait.until(ec.visibility_of_element_located((By.LINK_TEXT, f"{link_text}")))
    element.click()
    time.sleep(2)
    windows_list = driver.window_handles
    driver.switch_to.window(windows_list[1])
    search_element3 = wait.until(ec.visibility_of_element_located((By.NAME, "q")))
    search_element3.send_keys(f"Screen{temp}")
    time.sleep(2)
    driver.close()
    driver.switch_to.window(windows_list[0])
    temp += 1


driver.close()











