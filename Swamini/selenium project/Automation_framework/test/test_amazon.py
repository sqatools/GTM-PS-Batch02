import pytest
from modules.login.locator_function import amazonwebsite
from utilities.utils import read_json_file

@pytest.mark.usefixtures("initiate_driver") #conftest file
class TestamazonWebsite:

    @pytest.fixture(autouse=True)
    def setup(self):
        self.aw = amazonwebsite(self.driver) # locator function class
        self.json_data = read_json_file()   #test data json file

    def login(self):
        self.aw.login_page(
            email_id=self.json_data['amazon']['test2']['email_id'],
            password=self.json_data['amazon']['test1']['password']
        )
