from base.selenium_base import SeleniumBase
from .login_locator import *
import time


class Login(SeleniumBase):
    def __init__(self, driver):
        super().__init__(driver)

    def open_login_page(self):
        self.move_to_element(home_page_signup_locator)
        self.click_to_element(sign_in_locator)
        time.sleep(3)

    def enter_username(self, username):
        self.enter_values(email_input_locator, username)

    def enter_password(self, password):
        self.enter_values(password_input_locator, password)

    def submit_username(self):
        self.click_element(submit_btn_locator)

    def submit_password(self):
        self.click_element(sign_in_final_submit_btn_locator)

    def verify_incorrect_email(self):
        invalid_email_txt = self.get_text(incorrect_email_pwd_msg_locator)
        try:
            if invalid_email_txt =='We cannot find an account with that email address' or 'We cannot find an account with that mobile number':
                print(f"Error, {invalid_email_txt}")
            else:
                print(f"Error found")
        except Exception as e:
            print(f"Error")
            raise

    def verify_incorrect_password(self):
        invalid_pwd_txt = self.get_text(incorrect_email_pwd_msg_locator)
        try:
            if invalid_pwd_txt == 'Your password is incorrect':
                print(f"Error, {invalid_pwd_txt}")
            else:
                print(f"Error found")
        except Exception as e:
            print(f"Error")
            raise

# ------------------------------------ Function Start Here ------------------------------------------------#

    def incorrect_email_login(self,
                     incorrect_username:str,
                     correct_password:str):
        self.open_login_page()
        self.enter_username(incorrect_username)
        self.submit_username()
        self.verify_incorrect_email()

    def incorrect_password_login(self,
                                 correct_username:str,
                                 incorrect_password:str):
        self.open_login_page()
        self.enter_username(correct_username)
        self.submit_username()
        time.sleep(2)
        self.enter_password(incorrect_password)
        self.submit_password()
        self.verify_incorrect_password()


    def login_success(self,
                      correct_username:str,
                      correct_password:str):
        self.open_login_page()
        self.enter_username(correct_username)
        self.submit_username()
        self.enter_password(correct_password)
        self.submit_password()
