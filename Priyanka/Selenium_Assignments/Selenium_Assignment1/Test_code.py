import time

from Locators import *
from Function_Lib import *
from Test_data import *


get_driver(website_url, "Chrome", timeout=30)

# Choose the correct option:
click_element(loct_choose_option)

# Passenger Details
send_data(first_name,loct_first_name)
send_data(last_name,loct_last_name)
click_element(loct_female)

# Number of Additional Passangers
select_Value_dropdown(loct_number_passangers,"only one traveler")

# Travel Details
click_element(loct_trip)
send_data(source_city_name, fromcity_locator)
send_data(dest_city_name, destination_locator)

# Delivery Option

# How will you like to receive the dummy ticket(optional)
click_element(loct_dummy_ticket)

# Billing Details
send_data(billing_name, loct_billing_name)
send_data(billing_phone, loct_billing_phone)
send_data(billing_address, loct_billing_address)
send_data(billing_email, loct_billing_email)
send_data(postcode, loct_postcode)
send_data(Prefecture, loct_Prefecture)
send_data(address1, loct_street_address1)
send_data(address2, loct_street_address2)

#Most Visited Cities


