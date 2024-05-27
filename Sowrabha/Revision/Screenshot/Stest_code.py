import time

from Smain_code import *
from Slocator_code import *
from Stest_data import *

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
send_data(str_add,street_locator)
#click_element(checkbox_locator)
cur_header_text = get_text(Header_locator)
assert cur_header_text==web_heading
time.sleep(10)
