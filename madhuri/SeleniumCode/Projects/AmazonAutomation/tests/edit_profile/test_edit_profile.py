import time
import pytest
from data.amazon_data import *
from modules.edit_profile.edit_profile import EditProfile
from modules.login.login_class import Login

@pytest.mark.usefixtures("initiate_driver")
class TestEditProfile:

    @pytest.fixture(autouse=True)
    def setup(self):
        self.ep = EditProfile(self.driver)
        self.lg = Login(self.driver)

    def test_login_before_edit(self):
        self.rp.login_user(
            username=amazon_test_data['login']['correct_mobile'],
            password=amazon_test_data['login']['correct_password']
        )
        assert self.driver.title == amazon_test_data['page_title']['home_page_title']

    def test_update_profile_information(self):
        self.ep.edit_profile_info(fullname=amazon_test_data['edit_profile']['fullname'])
        time.sleep(10)



