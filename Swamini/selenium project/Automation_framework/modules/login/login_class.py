from base.selenium_base import selenium_base
from .login_locator import *

import time

class Login(selenium_base):
    def __init__(self,driver):
        super().__init__(driver)

    def click_signin_locator(self):
        self.click_element(click_sign_in_locator)

    def emailid_locator(self,email_id):
        self.enter_value(enteremail_locator,email_id)

    def click_continue_button(self):
        self.click_element(click_continue_locator)

    def enter_password(self,password):
        self.enter_value(enter_password_locator,password)

    def click_signin(self):
        self.click_element(signin_locator)

    def incorrect_email(self):
        invalid_email_txt = self.get_text(incorrect_email_pwd_msg_locator)
        try:
            if invalid_email_txt == 'We cannot find an account with that email address' or 'We cannot find an account with that mobile number':
                print(f"Error, {invalid_email_txt}")
            else:
                print(f"Error found")
        except Exception as e:
            print(f"Error")
            raise

    def incorrect_password(self):
        invalid_pass_text=self.get_text(incorrect_email_pwd_msg_locator)
        try:
            if invalid_pass_text=='Your password is incorrect':
                print(f"Error",{invalid_pass_text})
            else:
                print(f"error found")

        except Exception as e:
            print(f"error")
            raise

    def incorrect_email_login(self,incorrect_username:str):
        self.click_signin_locator()
        self.emailid_locator(incorrect_username)
        self.click_continue_button()
        self.incorrect_email()

    def incorrect_pass_login(self,email_id:str,incorrect_password:str):
        self.driver.refresh()
        self.clear_email_id()
        self.emailid_locator(email_id)
        self.click_continue_button()
        self.enter_password(incorrect_password)
        self.click_signin()
        self.incorrect_password()

    def correct_login(self,email_id:str,password:str):
        self.click_signin_locator()
        self.emailid_locator(email_id)
        self.click_continue_button()
        self.enter_password(password)
        self.click_signin()

