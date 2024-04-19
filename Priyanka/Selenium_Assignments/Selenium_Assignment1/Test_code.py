import time
from datetime import datetime

from selenium.webdriver import Keys
from Locators import *
from Function_Lib import *
from Test_data import *

get_driver(website_url, "Chrome", timeout=30)

# Choose the correct option:
click_element(loct_choose_option)

# Passenger Details
send_data(first_name, loct_first_name)
send_data(last_name, loct_last_name)
click_element(loct_female)

# Number of Additional Passangers
element = get_element(loct_number_passangers)
ele_select = Select(element)
ele_select.select_by_index(2)
# select_Value_dropdown(loct_number_passangers,Additional_Passangers)

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
select_Value_dropdown(loct_Country,Country)

#Most Visited Cities
click_element(loct_Most_Visited_Cities)

# Date of birth*
"""element = get_element(loct_birthday)
element.click()
element.send_keys("13")
element.send_keys("6")
element.send_keys(Keys.TAB)
element.send_keys("2000")"""

element = get_element(loct_birthday)
element.send_keys(Birthday)

element_Departure_Date = get_element(loct_Departure_Date)
element_Departure_Date.send_keys(Departure_Date)

element_Return_Date = get_element(loct_Return_Date)
element_Return_Date.send_keys(Return_Date)

element_visa_Date = get_element(loct_visa_Date)
element_visa_Date.send_keys(visa_Date)

# webpage screenshot
var = datetime.now().strftime("%d_%m_%Y_%H_%M_%S")
driver.save_screenshot(f"webpage{var}.png")

time.sleep(20)
driver.close()