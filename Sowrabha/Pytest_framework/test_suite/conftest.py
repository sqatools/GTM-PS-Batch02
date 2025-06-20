import pytest
from selenium import webdriver
from  selenium.webdriver.common.by import By
@pytest.fixture(scope="session",autouse=True)
def greeting():
    print("_________execution started____________")
    yield
    print("______________execution end________")

#command to executed
#python -m pytest -v -s -m smoke
#here we can execute the cases from the entire test suite [where ever smoke mark is mentioned all the files will get executed]

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

