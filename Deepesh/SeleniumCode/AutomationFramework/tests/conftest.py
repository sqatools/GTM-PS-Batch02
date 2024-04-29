import pytest
from data.session_data import *
from selenium import webdriver
from base.driver_factory import WebDriverFactory



@pytest.fixture(scope="class")
def initiate_driver(request):
    wf = WebDriverFactory(BROWSER, URL)
    driver = wf.get_driver()
    request.cls.driver = driver
    yield
    driver.close()

