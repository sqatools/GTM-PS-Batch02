import pytest
from modules.api.auth_api_module.auth_api_class import AuthAPI


class TestAuthAPI:

    @pytest.fixture(autouse=True)
    def setup(self):
        self.ap = AuthAPI()

    def test_verify_number_of_users(self):
        response = self.ap.get_all_users_details()
        assert response.status_code == 200
        assert response.text != []

    def test_verify_number_of_posts(self):
        response = self.ap.get_all_posts_details()
        assert response.status_code == 200
        assert response.text != []

    def test_verify_number_of_comments(self):
        response = self.ap.get_all_comments()
        assert response.status_code == 200
        assert response.text != []

    def test_verify_do_list(self):
        response = self.ap.get_all_to_do_list()
        assert response.status_code == 200
        assert response.text != []



