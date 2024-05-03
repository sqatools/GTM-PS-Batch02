import pytest
from modules.api.auth_api_module.auth_api_class import AuthAPI


class TestAuthAPI:

    @pytest.fixture(autouse=True)
    def setup(self):
        self.ap = AuthAPI()

    def test_verify_number_of_users(self):
        response = self.ap.get_all_users_details()
        print(response.text)
        assert response.status_code == 200

