import pytest
from Entity.login_class import AmazonBase
from Testdata.amazon_page_test_data import *

@pytest.mark.usefixtures("initiate_driver")
class TestAmazonLogin:

    @pytest.fixture(autouse=True)
    def setup(self):
        self.amazon_login = amazonlogin(self.driver)

    def test_booking_ticket(self):
        self.dw.provide_journey_details(
            first_name=user_details['first_name'],
            last_name=user_details['last_name'],
            dob=user_details['DOB'],
            from_city=user_details['from_city'],
            dest_city=user_details['dest_city']
        )