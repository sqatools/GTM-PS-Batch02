from base.selenium_base import selenium_base
from .simple_locator import *
import time

class AmazonWebsite(selenium_base):
    def __init__(self, driver):
        super().__init__(driver)
#2.Verify login is successful with correct email and password.
    def click_signin_button(self):
        self.click_element(click_sign_in_locator)

    def enter_emailid(self, email_id):
        self.enter_value(enteremail_locator, email_id)

    def click_continue(self):
        self.click_element(click_continue_locator)

    def enter_password(self, password):
        self.enter_value(enter_password_locator, password)

    def click_submit(self):
        self.click_element(signin_locator)

    def login_page(self, email_id: str,
                   password:str):
        self.click_signin_button()
        self.enter_emailid(email_id)
        time.sleep(5)
        self.click_continue()
        self.enter_password(password)
        time.sleep(5)
        self.click_submit()
        time.sleep(5)
#4.check if a user can successfully edit their profile information.
    def click_profile(self):
        self.click_element(click_profile_locator)

    def profile_arrow(self):
        self.click_element(profile_arrow_locator)

    def pencil_arrow(self):
        self.click_element(click_pencilarrow_locator)

    def profile_name_update(self, profile_name_update):
        self.enter_value(profilename_locator, profile_name_update)

    def profile_save(self):
        self.click_element(profile_save_locator)

    def get_profile_text(self):
        return self.get_text(profile_text_locator)

    def profile_page(self,profile_name_update:str):
        self.click_signin_button()
        self.click_profile()
        self.profile_arrow()
        self.pencil_arrow()
        self.profile_name_update(profile_name_update)
        self.profile_save()
        self.get_profile_text()


#5 Test searching for products using its name like shoe
    def send_element(self,search_name):
        self.enter_value(search_locator,search_name)

    def click_search(self):
        self.click_element(clicksearch_locator)

    def search_shoe(self,search_name:str):
        self.send_element(search_name)
        self.click_search()
