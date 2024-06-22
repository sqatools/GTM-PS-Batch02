import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(15)
driver.get("https://automationbysqatools.blogspot.com/2021/05/dummy-website.html")
def test_First_name():
    First_name=driver.find_element(By.NAME,"firstname")
    First_name.send_keys("RAM")
def test_correct_option():
    Ticket=driver.find_element(By.XPATH,"//span[text()='Dummy return ticket - $300 ']")
    Ticket.click()
    time.sleep(10)



