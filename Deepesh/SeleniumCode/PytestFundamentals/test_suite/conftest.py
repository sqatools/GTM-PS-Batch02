import pytest
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
import pytest


@pytest.fixture(scope="session", autouse=True)
def greeting():
    print("--- Welcome to Pytest Framework ----")
    yield
    print("--- Pytest execution has been completed ----")


@pytest.fixture(scope="function")
def setup():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.implicitly_wait(15)
    driver.get("https://automationbysqatools.blogspot.com/2021/05/dummy-website.html")
    return driver


@pytest.fixture(scope="module")
def setup_m():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.implicitly_wait(15)
    driver.get("https://automationbysqatools.blogspot.com/2021/05/dummy-website.html")
    return driver
