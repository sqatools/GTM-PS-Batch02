from base.selenium_base import SeleniumBase
from .edit_profile_locator import *
from  data.edit_profile_data import *
import time


class EditProfile(SeleniumBase):
    def __init__(self, driver):
        super().__init__(driver)

    def open_edit_profile(self):
        # check user is login or not
        #  if not login then redirect back to login page
        self.click_element(profile_name_locator)

    def click_to_your_account(self):
        self.click_element(your_account_nav_locator)

    def click_to_your_address(self):
        self.click_element(your_address_locator)

    def click_to_edit_address(self):
        self.click_element(edit_address_locator)

    def clear_previous_fullname(self):
        self.clear_input(edit_full_name_locator)

    def enter_fullname(self, fullname):
        self.enter_values(edit_full_name_locator, fullname)

    def submit_profile(self):
        self.click_element(submit_profile_locator)


# ------------------------------------ Function Start Here ------------------------------------------------#

    def edit_profile_info(self, fullname: str):
        self.open_edit_profile()
        self.click_to_your_account()
        self.click_to_your_address()
        self.click_to_edit_address()
        self.clear_previous_fullname()
        self.enter_fullname(fullname)
        self.submit_profile()

        
