import time

import pytest
from data.login_data import *
from modules.login.login_class import Login


@pytest.mark.usefixtures("initiate_driver")
class TestLogin:

    @pytest.fixture(autouse=True)
    def setup(self):
        self.lg = Login(self.driver)

    def test_invalid_email_login(self):
        self.lg.incorrect_email_login(
            incorrect_username = incorrect_mobile,
            correct_password = correct_password
        )


    def test_invalid_pwd_login(self):
        self.lg.incorrect_password_login(
            correct_username = correct_mobile,
            incorrect_password = incorrect_password
        )

    def test_login_success(self):
        self.lg.login_success(
            correct_username = correct_mobile,
            correct_password = correct_password
        )
        time.sleep(10)








