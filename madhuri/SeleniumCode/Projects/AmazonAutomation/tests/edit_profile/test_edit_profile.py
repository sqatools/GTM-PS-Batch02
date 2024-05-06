import time

import pytest
from data.edit_profile_data import *
from data.login_data import *
from modules.edit_profile.edit_profile import EditProfile
from modules.login.login_class import Login

@pytest.mark.usefixtures("initiate_driver")
class TestEditProfile:

    @pytest.fixture(autouse=True)
    def setup(self):
        self.ep = EditProfile(self.driver)
        self.lg = Login(self.driver)

    def test_login_before_edit(self):
        self.lg.login_success(
            correct_username=correct_mobile,
            correct_password=correct_password
        )

    def test_update_profile_information(self):
        self.ep.edit_profile_info(fullname=fullname)
        time.sleep(10)



