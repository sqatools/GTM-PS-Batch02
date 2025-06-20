import time
from selenium_main1 import *
from locator import *
from test_data1 import *
get_driver(website_url, "Chrome", timeout=30)

#2 Verify login is successful with correct email and password.

click_element(click_sign_in_locator)
send_element(emailid,enteremail_locator)
click_element(click_continue_locator)
send_element(password,enter_password_locator)
click_element(signin_locator)


time.sleep(5)
#4 Check if a user can successfully edit their profile information.

click_element(click_sign_in_locator)
click_element(click_profile_locator)
click_element(profile_arrow_locator)
click_element(click_pencilarrow_locator)
send_element(profilename,profilename_locator)
click_element(profile_save_locator)
get_text(profile_text_locator)
time.sleep(5)

#5 Test searching for products using its name like shoe

send_element(shoe,search_locator)
click_element(clicksearch_locator)