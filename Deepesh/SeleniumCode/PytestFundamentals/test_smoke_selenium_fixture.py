"""
command to install pytest
"""
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
import pytest

@pytest.fixture(scope="function")
def setup():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.implicitly_wait(15)
    driver.get("https://automationbysqatools.blogspot.com/2021/05/dummy-website.html")
    return driver


def test_choose_ticket_price(setup):
    driver = setup
    price_locator = "//span[contains(text(), 'Dummy hotel booking ticket - $400 ')]//preceding-sibling::input"
    price_element = driver.find_element(By.XPATH, price_locator)
    price_element.click()
    time.sleep(5)


def test_user_details(setup):
    driver = setup
    first_name = driver.find_element(By.XPATH, "(//input[@id='firstname'])[1]")
    first_name.send_keys("John")
    last_name = driver.find_element(By.XPATH, "(//input[@id='firstname'])[2]")
    last_name.send_keys("Doe")
    time.sleep(5)


def test_select_dob(setup):
    driver = setup
    dob_element = driver.find_element(By.ID, "birthday")
    dob_element.send_keys("04/16/2024")
    time.sleep(5)
