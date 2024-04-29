import pytest
from modules.dummy.dummy_page_class import DummyWebsite
from data.dummy_page_test_data import *

@pytest.mark.usefixtures("initiate_driver")
class TestDummyWebsite:

    @pytest.fixture(autouse=True)
    def setup(self):
        self.dw = DummyWebsite(self.driver)

    def test_booking_ticket(self):
        self.dw.provide_journey_details(
            first_name=user_details['first_name'],
            last_name=user_details['last_name'],
            dob=user_details['DOB'],
            from_city=user_details['from_city'],
            dest_city=user_details['dest_city']
        )

    def test_provide_billing_details(self):
        self.dw.provide_billing_details(
            billing_name=user_details['billing_name'],
            billing_phone=user_details['billing_phone'],
            billing_email=user_details['billing_email'],
            billing_address=user_details['billing_address'],
            billing_postal_code=user_details['billing_postal_code'],
            billing_prefecture=user_details['billing_prefecture'],
        )



