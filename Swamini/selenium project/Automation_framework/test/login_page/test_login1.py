import pytest
from modules.login.locator_function1 import AmazonWebsite
from utilities.utils import read_json_file
import time

@pytest.mark.usefixtures("initiate_driver")
class TestAmazonWebsite:
    @pytest.fixture(autouse=True)
    def setup(self):
        self.AW = AmazonWebsite(self.driver)
        self.json_data = read_json_file()

    def test_login(self):
        self.AW.login_page(
            email_id=self.json_data['amazon']['test2']['email_id'],

            password=self.json_data['amazon']['test1']['password']
        )

    def test_profile_page(self):
        self.AW.profile_page(

        profile_name_update=self.json_data['amazon']['test4']['profile_name_update'])

    def test_search_shoe(self):
        self.AW.search_shoe(
            search_name=self.json_data['amazon']['test5']['search_name']
        )

