import pytest
from data.Amazon_testdata import *
from modules.Amazon_page_class import Amazon_modules

@pytest.mark.usefixtures("initiate_driver")
class TestcasesAmazon:

    @pytest.fixture(autouse=True)
    def setup(self):
        self.Amazon = Amazon_modules(self.driver)
