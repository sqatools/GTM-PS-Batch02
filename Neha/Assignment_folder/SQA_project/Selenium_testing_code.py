import time

from SQA_Locator import *
from functions_file import *
from Testdata_file import *
from selenium.webdriver.support.select import Select


get_driver(web_URL ,'Chrome',timeout=35)

#Ticket Booking Options
click_radio_option(choose_ticket_option_locator)

# Passenger Details
ec_passenger_heading= get_text(passenger_heading_locator)
assert ec_passenger_heading == passenger_heading
send_data(Firstname, Firstname_locator)
send_data(LastName, LastName_locator)
send_data(DOB, DOB_locator)
click_element(male_rdbtn_locator)
click_element(female_rdbtn_locator)

##Additinal travel info (dropdown)
select_dropdown_value(dropdown_locator,"2" )
# element = get_element(dropdown_locator)
# select_obj = Select(element)
# time.sleep(5)
# select_obj.select_by_visible_text(" Add 1 more passenger (100%)  ")
# select_obj.select_by_value("4")
# time.sleep(5)


#Travel Details
ec_travel_details_heading = get_text(Travel_details_heading_locator)
assert ec_travel_details_heading == Travel_details_heading
click_element(Oneway_locator)
click_element(roundtrip_locator)
send_data(from_city,fromcity_locator)
send_data(destination_city,destcity_locator)

##Delivery Details
ec_delivery_option_heading = get_text(delivery_option_heading_locator)
assert ec_delivery_option_heading == Delivery_option_heading
send_data(Visa_interview_date,Visa_interview_locator)
click_element(Email_locator)
click_element(whatsapp_locator)
click_element(Both_locator)

##Billing Details
ec_billing_option_heading = get_text(billing_option_heading_locator)
assert ec_billing_option_heading == billing_option_heading
send_data(Billing_name,Billing_name_locator)
send_data(Billing_phone,Billing_phone_locator)
send_data(Email_id,Email_id_locator)
send_data(Street_Address,Street_Address_locator)
select_dropdown_value(Country_locator, "AX")
#select_dropdown_value = get_element(Country_locator,"Algeria")
# element = get_element(Country_locator)   #(dropdown)
# select_obj1 = Select(element)
# time.sleep(5)
# select_obj1.select_by_visible_text("Algeria")
# # select_obj1.select_by_value("AX")
# # select_obj1.select_by_index("5")
send_data(Postal,Postal_Locator)
send_data(prefecture,prefecture_locator)
send_data(Street_add1,Street_add1_locator)
send_data(Street_add2,Street_add2_locator)


#Checkboxes scenario-Most visited cities
checkbox = click_elements(most_visited_cities_locator)
