import pytest
from modules.api.mobile_api_module.mobile_api_class import MobileAPI


class TestMobileAPITestCases:

    @pytest.fixture(autouse=True)
    def setup(self):
        self.rest_api = MobileAPI()

    def test_verify_all_mobile_details_received(self):
        status_code, response = self.rest_api.get_all_mobile_details()
        assert status_code == 200
        assert len(response) == 13
