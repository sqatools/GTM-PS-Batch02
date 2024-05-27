import time

from Emain_code import *
from Elocator_code import *
from Etest_data import *

get_driver()
send_keys('rahul',first_name_locator)
send_keys('shetty',last_name_locator)

#click_element(correct_option_locator)
send_keys('10/10/1996',DOB_locator)
click_element(gender_locator)
send_keys("Bengaluru",from_city_locator)
send_keys("mumbai",dest_city_locator)
send_keys("12/6/1024",departure_locator)
send_keys("15/6/2024",return_locator)
send_keys("10/6/1024",Visa_locator)
send_keys("Rahul",Billing_loctor)
send_keys(str_add,street_locator)
#click_element(checkbox_locator)
cur_header_text = get_text(Header_locator)
assert cur_header_text==web_heading
time.sleep(10)
