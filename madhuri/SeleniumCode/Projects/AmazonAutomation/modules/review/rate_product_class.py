from base.selenium_base import SeleniumBase
from .rate_product_locator import *
import time


class ReviewProduct(SeleniumBase):
    def __init__(self, driver):
        super().__init__(driver)

    def open_login_page(self):
        self.move_to_element(sign_in_locator)
        self.click_to_element(sign_in_locator)
        time.sleep(3)

    def enter_username(self, username):
        self.enter_value(email_input_locator, username)

    def enter_password(self, password):
        self.enter_value(password_input_locator, password)

    def login_user(self,
                   username: str):
        self.open_login_page()
        self.enter_username(username)



    """
    move_to_element(home_page_signup_locator)
    click_to_element(sign_in_locator)
    time.sleep(3)

    # verify we are on registration page
    login_page_title = driver.title
    assert login_page_title == login_title

    click_element(submit_btn_locator)
    time.sleep(3)
    send_data(email_input_locator, mobile_number)
    time.sleep(3)
    click_element(submit_btn_locator)
    time.sleep(3)
    send_data(password_input_locator, password)
    time.sleep(3)
    click_element(sign_in_final_submit_btn_locator)

    # OTP Before Login
    # time.sleep(20)
    # click_element(send_otp_button_locator)
    # time.sleep(5)

    after_login_page_title = driver.title
    print('after login page title: ', after_login_page_title)
    print('home page title: ', home_page_title)
    assert after_login_page_title == home_page_title
    time.sleep(5)
    """