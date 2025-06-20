import pytest
# from data.session_data import *
# from selenium import webdriver
from base.driver_factory import WebDriverFactory


URL = "https://automationbysqatools.blogspot.com/2021/05/dummy-website.html"
BROWSER = 'chrome'
# headless = False  # This will not launch if it True, it will execute in headless,


@pytest.fixture(scope="class")
def initiate_driver(request):
    wf = WebDriverFactory(BROWSER, URL)
    driver = wf.get_driver()
    request.cls.driver = driver
    yield
    driver.close()

