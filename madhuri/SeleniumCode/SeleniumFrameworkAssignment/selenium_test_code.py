import time

from selenium_waits_code import *
from selenium_locators import *
from selenium_test_data import *

driver, wait = get_driver()

# driver.save_screenshot("screenshots\webpage2.png")

#Ticket Booking Options
element_dd = select_radio_option(radio_option, choose_ticket_option_locator)
# to take element screenshot
# element_dd.screenshot("screenshots\web_element.png")

# click_radio_option(choose_ticket_option_locator)
time.sleep(2)

# Passenger Details
ec_passenger_heading= get_text(passenger_heading_locator)
assert ec_passenger_heading == passenger_heading
send_data(first_name, first_name_locator)
time.sleep(2)
send_data(last_name, last_name_locator)
time.sleep(2)
send_data(dob, dob_locator)
time.sleep(2)
click_element(female_locator)
time.sleep(2)

# No. of Additional Passenger
select_dropdown_by_value(travel_person_count, traveler_dropdown_locator)
time.sleep(2)

#Travel Details
ec_traveldetails_heading = get_text(traveldetails_heading_locator)
assert ec_traveldetails_heading == traveldetails_heading
time.sleep(2)

click_element(oneway_trip_locator)
send_data(source_city_name, source_city_locator)
time.sleep(2)
send_data(dest_city_name, destination_city_locator)
time.sleep(2)
send_data(departdate, departdate_locator)
time.sleep(2)
send_data(returndate, returndate_locator)

# Delivery Option
ec_deliveryoption_heading = get_text(deliveryoption_heading_locator)
assert ec_deliveryoption_heading == deliveryoption_heading
send_data(visadate,visadate_locator)
time.sleep(2)
click_element(ticket_by_whatsapp_locator)
time.sleep(2)

# Billing Details
ec_billing_heading = get_text(billing_heading_locator)
assert ec_billing_heading == billing_heading_text
send_data(billing_name, billing_name_locator)
time.sleep(2)
send_data(billing_phone, billing_phone_locator)
time.sleep(2)
send_data(billing_email, billing_email_locator)
time.sleep(2)
send_data(billing_address, billing_address_locator)
time.sleep(2)
select_dropdown_by_visible_text(billing_country, billing_country_locator)
time.sleep(2)
send_data(billing_postcode, billing_postcode_locator)
time.sleep(2)
send_data(billing_prefecture, billing_prefecture_locator)
time.sleep(2)
send_data(billing_street_address1, billing_street_address1_locator)
time.sleep(2)
send_data(billing_street_address2, billing_street_address2_locator)
time.sleep(2)


# Most Visited Cities
click_citi_options(cities_checkbox_options_locator)
# select_checkboxes(select_checkboxes_values, cities_checkbox_options_locator)
# driver.save_screenshot("screenshots\webpage.png")

