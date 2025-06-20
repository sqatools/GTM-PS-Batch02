import time
from datetime import datetime

# custom file
from amazon_locator import *
from amazon_functions import *
from amazon_data import *

driver, wait = get_driver()
# action_chain -> click on registration page
move_to_element(home_page_signup_locator)
click_to_element(start_here_text_locator)

# verify we are on registration page
reg_page_title = driver.title
assert reg_page_title == create_account_page_title

# registration form
# how to verify after submit it should show error message
element = click_element(verify_mobile_btn_locator)

send_data(customer_name_locator, name)
send_data(phone_number_locator, mobile_number)
send_data(password_locator, password)
element = click_element(verify_mobile_btn_locator)

time.sleep(15)

