import pytest
from data.session_data import *
from selenium import webdriver


@pytest.fixture(scope="class")
def initiate_driver(request):
    driver = webdriver.Chrome()
    driver.get(URL)
    driver.maximize_window()
    request.cls.driver = driver

