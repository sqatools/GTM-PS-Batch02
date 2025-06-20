import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time


def test_choose_ticket_price(setup):
    driver = setup
    price_locator = "//span[contains(text(), 'Dummy hotel booking ticket - $400 ')]//preceding-sibling::input"
    price_element = driver.find_element(By.XPATH, price_locator)
    price_element.click()
    time.sleep(5)


@pytest.mark.parametrize("fname, lname ", [('pratik', 'chouhan'), ('Neha', 'sharma'), ('Kiran', 'Gupta')])
def test_user_details(setup, fname, lname):
    driver = setup
    first_name = driver.find_element(By.XPATH, "(//input[@id='firstname'])[1]")
    first_name.clear()
    first_name.send_keys(fname)
    last_name = driver.find_element(By.XPATH, "(//input[@id='firstname'])[2]")
    last_name.clear()
    last_name.send_keys(lname)
    time.sleep(2)

@pytest.mark.parametrize("dob", ["04/16/2024", "04/16/2025", "04/16/2026"])
def test_select_dob(setup, dob):
    driver = setup
    dob_element = driver.find_element(By.ID, "birthday")
    dob_element.clear()
    dob_element.send_keys(dob)
    time.sleep(5)