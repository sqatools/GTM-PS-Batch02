import time

from selenium_main_code import *
from selenium_locator_code import *

get_driver()
send_data('rahul',first_name_locator)
send_data('shetty',last_name_locator)
#click_element(correct_option_locator)
send_data('10/10/1996',DOB_locator)
click_element(gender_locator)
send_data("Bengaluru",from_city_locator)
send_data("mumbai",dest_city_locator)
send_data("12/6/1024",departure_locator)
send_data("15/6/2024",return_locator)
send_data("10/6/1024",Visa_locator)
send_data("Rahul",Billing_loctor)
#click_element(checkbox_locator)
time.sleep(10)
