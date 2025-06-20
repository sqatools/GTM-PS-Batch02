import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.action_chains import ActionChains
import time
from amazon_functions import *



def test_login_user():
    element_menu = get_element((By.XPATH, "//*[contains(text(),'Account & Lists')]"))
    move_to_element(element_menu)
    time.sleep(5)
    print('here')

    tool_tip = get_element((By.XPATH, "(//div[@id='nav-flyout-accountList']//following::a[contains(text(), 'Start here')])[1]"))
    click_to_element(tool_tip)
    time.sleep(10)

