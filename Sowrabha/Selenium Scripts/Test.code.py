import time

from selenium_common_ import *
from Locators import *
from Testdata import *

get_driver(website_url, "Chrome", timeout=30)
#click_element(Ticket_locator)
send_data('rahul', first_name_locator)
send_data('Gupta', last_name_locator)
send_data(B_name, Billingname_locator)
send_data(B_phone,phone_locator)
send_data(B_email,email_locator)

send_data(B_address,street_locator)
send_data(B_postcode,post_locator)
send_data(B_Prefecture,prefecture_locator)
send_data(S1_address,S_address_locator)
send_data(S2_address,S1_address_locator)
#click_element(place_locator)
time.sleep(10)
#send_data(Birthday,DOB_locator)
#send_data('06/06/1996',DOB_locator)
click_element(male_locator)
click_element(female_locator)
click_element(Trip_locator)
click_element(Msg_locator)
send_data(source_city_name, fromcity_locator)
send_data(dest_city_name, destination_locator)
send_data(Birthday,DOB_locator)
click_element(checkbox_locator)
select_dropdown_value(country_dropdown_locator, country_name)
time.sleep(5)



