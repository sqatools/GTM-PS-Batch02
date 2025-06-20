import time

from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec

Links = ["What is Software Testing" ,"What is Manual Testing", "Software Testing Principles"]
temp=1

driver = webdriver.Chrome()
wait = WebDriverWait(driver, 15, 0.5)
driver.get("https://automationbysqatools.blogspot.com/p/manual-testing.html")
driver.maximize_window()
Links = ["What is Software Testing","What is Manual Testing", "Software Testing Principles"]

temp = 1
for link_text in Links:
    element_1 = wait.until(ec.visibility_of_element_located((By.LINK_TEXT, f"{link_text}")))
    element_1.click()
    time.sleep(10)
    window_list=driver.window_handles
    driver.switch_to.window(window_list[0])
    element_1=wait.until(ec.visibility_of_element_located((By.NAME,"q")))
    element_1.send_keys(f"screen{temp}")
    time.sleep(2)
    driver.switch_to.window(window_list[0])
    time.sleep(10)
    temp=temp+1

