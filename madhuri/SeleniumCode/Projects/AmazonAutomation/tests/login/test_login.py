import pytest
from data.amazon_data import *
from modules.login.login_class import Login


@pytest.mark.usefixtures("initiate_driver")
class TestLogin:

    @pytest.fixture(autouse=True)
    def setup(self):
        self.lg = Login(self.driver)

    def test_invalid_email_login(self):
        self.lg.incorrect_email_login(
            incorrect_username = amazon_test_data['login']['incorrect_mobile'],
            correct_password = amazon_test_data['login']['correct_password']
        )


    def test_invalid_pwd_login(self):
        self.lg.incorrect_password_login(
            correct_username = amazon_test_data['login']['correct_mobile'],
            incorrect_password = amazon_test_data['login']['incorrect_password']
        )

    def test_login_success(self):
        self.lg.login_success(
            correct_username = amazon_test_data['login']['correct_mobile'],
            correct_password = amazon_test_data['login']['correct_password']
        )
        assert self.driver.title == amazon_test_data['page_title']['home_page_title']







