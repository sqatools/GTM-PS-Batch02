import time

############# POM Page Object Model #################

from Selenium_Waits_Code import *
from Selenium_Locators import *

get_driver(website_url,"Chrome",timeout=30)
send_data('Rahul',first_name_locator)
send_data('Gupta',last_name_locator)
time.sleep(5)

click_element(male_locator)
click_element(female_locator)