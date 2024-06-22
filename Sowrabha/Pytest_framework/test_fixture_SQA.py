import time

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

@pytest.fixture(scope="function")
def setup():
    driver= webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://automationbysqatools.blogspot.com/2021/05/dummy-website.html")
    time.sleep(10)
    return driver

def test_First_name(setup):
    driver=setup
    First_name=driver.find_element(By.NAME,"firstname")
    First_name.send_keys("RAM")
    time.sleep(5)
def test_correct_option(setup):
    driver=setup
    Ticket=driver.find_element(By.XPATH,"//span[text()='Dummy return ticket - $300 ']")
    Ticket.click()
    time.sleep(10)
