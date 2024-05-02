import pytest
from modules.dummy.dummy_page_class import DummyWebsite
from data.dummy_page_test_data import *
from utilities.utils import read_json_file


@pytest.mark.usefixtures("initiate_driver")
class TestDummyWebsite:

    @pytest.fixture(autouse=True)
    def setup(self):
        self.dw = DummyWebsite(self.driver)
        self.json_data = read_json_file()

    def test_booking_ticket(self):
        self.dw.provide_journey_details(
            first_name=self.json_data['dummy']['test1']['first_name'],
            last_name=self.json_data['dummy']['test1']['last_name'],
            num_of_passenger=self.json_data['dummy']['test1']['select_pass'],
            dob=self.json_data['dummy']['test1']['DOB'],
            from_city=self.json_data['dummy']['test1']['from_city'],
            dest_city=self.json_data['dummy']['test1']['dest_city'],
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



