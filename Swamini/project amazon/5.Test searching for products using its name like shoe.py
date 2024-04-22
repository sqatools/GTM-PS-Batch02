import time
from selenium_main1 import *
from locator import *
from test_data1 import *
get_driver(website_url, "Chrome", timeout=30)

click_element(click_sign_in_locator)

send_element(emailid,enteremail_locator)
click_element(click_continue_locator)
send_element(password,enter_password_locator)
click_element(signin_locator)

send_element(shoe,search_locator)
click_element(clicksearch_locator)

time.sleep(5)