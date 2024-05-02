import pytest
from modules.login.locator_function import login
from utilities.utils import read_json_file
# from data.test_data import *
import time

@pytest.mark.usefixtures("initiate_driver") #conftest file
class TestAmazonWebsite:
    @pytest.fixture(autouse=True)
    def setup(self):
        self.log = login(self.driver) # locator function class
        self.json_data = read_json_file()   #test data json file

    def test_login(self):
        self.log.login_page(
            email_id=self.json_data['amazon']['test2']['email_id'],

            password=self.json_data['amazon']['test1']['password']
        )
