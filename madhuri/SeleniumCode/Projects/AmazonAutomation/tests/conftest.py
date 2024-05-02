import pytest
from data.session_data import *
from base.driver_factory import WebDriverFactory


@pytest.fixture(scope="class")
def initiate_driver(request):
    wf = WebDriverFactory(BROWSER, URL)
    driver = wf.get_driver()
    request.cls.driver = driver
    yield
    driver.close()


@pytest.fixture(scope="function")
def initiate_driver2(request):
    wf2 = WebDriverFactory(BROWSER, URL)
    driver = wf2.get_driver()
    request.cls.driver = driver
    yield
    driver.close()
