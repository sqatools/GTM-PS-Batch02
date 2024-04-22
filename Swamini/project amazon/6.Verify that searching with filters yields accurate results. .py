#Verify that searching with filters (e.g., category, price range) yields accurate results.


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

click_element(brandfilter_locator)
time.sleep(5)
click_element(rangefilter_locator)
click_element(alldiscount_locator)
click_element(size_locator)
# click_element(color_locator)


time.sleep(10)