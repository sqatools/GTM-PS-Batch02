import time

from selenium_main_code import *
from selenium_locator_code import *

get_driver()
send_data('rahul',first_name_locator)
send_data('shetty',last_name_locator)
time.sleep(10)