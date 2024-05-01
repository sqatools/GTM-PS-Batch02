from base.selenium_base import selenium_base
from .simple_locator import *
import time

class amazonwebsite(selenium_base):
    def __init__(self,driver):
        super().__init__(driver)
#2 Verify login is successful with correct email and password.
    def click_signin_button(self):
        self.click_element(click_sign_in_locator)

    def enter_emailid(self,email_id):
        self.enter_value(enteremail_locator,email_id)

    def click_continue(self):
        self.click_element(click_continue_locator)

    def enter_password(self,password):
        self.enter_value(enter_password_locator,password)

    def click_submit(self):
        self.click_element(signin_locator)


    # def login_page(self,email_id:str,
    #                password:str):
    #     self.click_signin_button()
    #     self.enter_emailid(email_id)
    #     time.sleep(5)
    #     self.click_continue()
    #     self.enter_password(password)
    #     time.sleep(5)
    #     self.click_submit()
    #     time.sleep(5)

class login(amazonwebsite):
    def __init__(self,driver, email_id, password):
        super().__init__(driver)
        self.email_id = email_id
        self.password = password
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


