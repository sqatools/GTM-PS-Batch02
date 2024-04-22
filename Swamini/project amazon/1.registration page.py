import time
from selenium_main1 import *
from locator import *
from test_data1 import *
get_driver(website_url, "Chrome", timeout=30)

#------------------#create Acoount for amazon :----------------------------------------------
#clicking the sign in button
click_element(click_sign_in_locator)

#clicking the  Create your Amazon account button
click_element(create_account_locator)

#enter email_id
send_element(full_name,entername_locator)

#enter mobile number
send_element(Mob_no,enter_mobno_locator)

#enter password
send_element(password,enter_password_locator)

#click verify your mobile number
click_element(click_continue_locator)

click_element(click_startpuzzle)
