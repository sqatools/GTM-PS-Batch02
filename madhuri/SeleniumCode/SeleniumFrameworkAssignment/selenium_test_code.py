import time

from selenium_waits_code import *
from selenium_locators import *
from selenium_test_data import *

driver, wait = get_driver()

#Ticket Booking Options

click_radio_option(choose_ticket_option_locator)

# Passenger Details
ec_passenger_heading= get_text(passenger_heading_locator)
assert ec_passenger_heading == passenger_heading
send_data(first_name, first_name_locator)
send_data(last_name, last_name_locator)
click_element(female_locator)

# No. of Additional Passenger

#Travel Details
ec_traveldetails_heading = get_text(traveldetails_heading_locator)
assert ec_traveldetails_heading == traveldetails_heading

click_element(oneway_trip_locator)
send_data(source_city_name, source_city_locator)
send_data(dest_city_name, destination_city_locator)
time.sleep(1)

# Delivery Option
ec_deliveryoption_heading = get_text(deliveryoption_heading_locator)
assert ec_deliveryoption_heading == deliveryoption_heading
click_element(ticket_by_whatsapp_locator)

time.sleep(3)

# Billing Details
ec_billing_heading = get_text(billing_heading_locator)
assert ec_billing_heading == billing_heading_text
send_data(billing_name, billing_name_locator)
send_data(billing_phone, billing_phone_locator)
send_data(billing_email, billing_email_locator)
send_data(billing_address, billing_address_locator)
send_data(billing_country, billing_country_locator)
send_data(billing_postcode, billing_postcode_locator)
send_data(billing_prefecture, billing_prefecture_locator)
send_data(billing_street_address1, billing_street_address1_locator)
send_data(billing_street_address2, billing_street_address2_locator)


# Most Visited Cities
time.sleep(5)


## doubts
# 1. multiple choose radio option
# 2. radio_element = driver.find_elements(By.XPATH, "//input[@type='radio']//parent::li") cant get value of radio button
# 3. short-cut key to rename multiple variables
