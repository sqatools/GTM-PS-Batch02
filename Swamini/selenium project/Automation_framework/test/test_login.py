import pytest
from modules.login.login_class import Login
from utilities.utils import read_json_file

@pytest.mark.usefixtures("initiate_driver")
class Test_login:
    @pytest.fixture(autouse=True)
    def setup(self):
        self.log = Login(self.driver)
        self.json_data = read_json_file()

    def test_invalid_email(self):
        self.log.incorrect_email_login(
            incorrect_username=self.json_data['amazon']['test1']['incorrect_username']

        )

    def test_invalid_pwd(self):
        self.log.incorrect_pass_login(
            email_id=self.json_data['amazon']['test2']['email_id'],
            incorrect_password=self.json_data['amazon']['test1']['incorrect_password']
        )

    def test_login_successful(self):
        self.log.correct_login(
            email_id=self.json_data['amazon']['test2']['email_id'],
            password=self.json_data['amazon']['test1']['password']
        )

