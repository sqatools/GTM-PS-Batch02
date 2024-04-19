"""
command to install pytest
"""
import time

import pytest
from selenium.webdriver.common.by import By
from test_data import *



def test_choose_ticket_price(setup_m):
    driver = setup_m
    price_locator = "//span[contains(text(), 'Dummy hotel booking ticket - $400 ')]//preceding-sibling::input"
    price_element = driver.find_element(By.XPATH, price_locator)
    price_element.click()
    time.sleep(5)


#@pytest.mark.parametrize("fname, lname ", [('pratik', 'chouhan'), ('Neha', 'sharma'), ('Kiran', 'Gupta')])
@pytest.mark.parametrize("fname, lname ", user_info)
def test_user_details(setup_m, fname, lname):
    driver = setup_m
    first_name = driver.find_element(By.XPATH, "(//input[@id='firstname'])[1]")
    first_name.clear()
    first_name.send_keys(fname)
    last_name = driver.find_element(By.XPATH, "(//input[@id='firstname'])[2]")
    last_name.clear()
    last_name.send_keys(lname)
    time.sleep(2)

@pytest.mark.parametrize("dob", ["04/16/2024", "04/16/2025", "04/16/2026"])
def test_select_dob(setup_m, dob):
    driver = setup_m
    dob_element = driver.find_element(By.ID, "birthday")
    dob_element.clear()
    dob_element.send_keys(dob)
    time.sleep(5)
