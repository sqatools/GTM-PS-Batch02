from base.selenium_base import SeleniumBase
from .dummy_page_class_data import *


class DummyWebsite(SeleniumBase):
    def __init__(self, driver):
        super().__init__(driver)

    def enter_first_name(self, first_name):
        self.enter_value(first_name_locator, first_name)

    def enter_last_name(self, last_name):
        self.enter_value(last_name_locator, last_name)

    def select_number_of_passenger(self, select_option):
        self.select_value_from_dropdown(select_number_of_passenger, select_option)

    def enter_dob(self, dob):
        self.enter_value(dob_locator, dob)

    def select_male_radio(self):
        self.click_element(male_locator)

    def enter_from_city(self, from_city):
        self.enter_value(from_city_locator, from_city)

    def enter_destination_city(self, dest_city):
        self.enter_value(dest_city_locator, dest_city)

    def provide_journey_details(self,
                                first_name: str,
                                last_name: str,
                                dob: str,
                                num_of_passenger: str,
                                from_city: str,
                                dest_city: str):
        self.enter_first_name(first_name)
        self.enter_last_name(last_name)
        self.enter_dob(dob)
        self.select_number_of_passenger(num_of_passenger)
        self.select_male_radio()
        self.enter_from_city(from_city)
        self.enter_destination_city(dest_city)

    def enter_billing_name(self, billing_name):
        self.enter_value(billing_name_locator, billing_name)

    def enter_billing_phone(self, billing_phone):
        self.enter_value(billing_phone_locator, billing_phone)

    def enter_billing_email(self, billing_email):
        self.enter_value(billing_email_locator, billing_email)

    def enter_billing_address(self, billing_address):
        self.enter_value(billing_address_locator, billing_address)

    def enter_postal_code(self, postal_code):
        self.enter_value(postcode_locator, postal_code)

    def enter_prefecture(self, prefecture):
        self.enter_value(prefecture_locator, prefecture)

    def provide_billing_details(self,
                                billing_name,
                                billing_phone,
                                billing_email,
                                billing_address,
                                billing_postal_code,
                                billing_prefecture,
                                ):
        self.enter_billing_name(billing_name)
        self.enter_billing_phone(billing_phone)
        self.enter_billing_email(billing_email)
        self.enter_billing_address(billing_address)
        self.enter_postal_code(billing_postal_code)
        self.enter_prefecture(billing_prefecture)
