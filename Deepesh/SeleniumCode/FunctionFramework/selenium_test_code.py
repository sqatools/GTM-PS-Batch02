import time

from selenium_function_code import *
from selenium_locators import *
from test_data import *

get_driver(website_url, "Chrome", timeout=30)
send_data(first_name, first_name_locator)
send_data(last_name, last_name_locator)
time.sleep(5)
click_element(male_locator)
click_element(female_locator)
send_data(source_city_name, fromcity_locator)
send_data(dest_city_name, destination_locator)
cur_header_text = get_text(header_locator)
assert cur_header_text == website_header
select_dropdown_value(country_dropdown_locator, country_name)
time.sleep(5)
select_dropdown_value(add_more_pass_dd_locator, add_more_pass_option)
time.sleep(5)





