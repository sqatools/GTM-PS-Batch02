import time

from go_method_code import *
from go_locators import *
from go_test_data import *

driver, wait = get_driver()

click_element(close_login_popup_locator)
time.sleep(2)
get_text(one_way_trip_locator)
send_data('Mumbai', from_input_locator)
send_data('Pune', to_input_locator)