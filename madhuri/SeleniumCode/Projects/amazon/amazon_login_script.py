import time
from amazon_locator import *
from amazon_functions import *
from amazon_data import *

driver, wait = get_driver()


def login_user():
    move_to_element(home_page_signup_locator)
    click_to_element(sign_in_locator)
    time.sleep(3)
    # verify we are on registration page
    login_page_title = driver.title
    assert login_page_title == login_title

    click_element(submit_btn_locator)
    time.sleep(3)
    send_data(email_input_locator,mobile_number)
    time.sleep(3)
    click_element(submit_btn_locator)
    time.sleep(3)
    send_data(password_input_locator, password)
    time.sleep(3)
    click_element(sign_in_final_submit_btn_locator)
    time.sleep(20)
    click_element(send_otp_button_locator)
    time.sleep(5)

    after_login_page_title = driver.title
    print(after_login_page_title)
    print(home_page_title)
    assert after_login_page_title == home_page_title
    time.sleep(5)