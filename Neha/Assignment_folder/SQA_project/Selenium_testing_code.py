import time

from SQA_Locator import *
from functions_file import *
from Testdata_file import *
from selenium.webdriver.support import select


get_driver(web_URL ,'Chrome',timeout=35)
send_data(Firstname, Firstname_locator)
send_data(LastName, LastName_locator)
time.sleep(5)
send_data(DOB, DOB_locator)
click_element(male_rdbtn_locator)
click_element(female_rdbtn_locator)


##Additinal travel info (dropdown)
element = get_element(dropdown_locator)
select_obj = Select(element)
time.sleep(5)
# select_obj.select_by_visible_text(" Add 1 more passenger (100%)  ")
select_obj.select_by_value("4")
time.sleep(5)


##travel Details
get_text(Travel_details_locator)
click_element(Oneway_locator)
click_element(roundtrip_locator)
time.sleep(5)
send_data(from_city,fromcity_locator)
send_data(destination_city,destcity_locator)

##Delivery Details
get_text(Deliveryoption_locator)
send_data(Visa_interview_date,Visa_interview_locator)
click_element(Email_locator)
click_element(whatsapp_locator)
click_element(Both_locator)

##Billing Details
send_data(Billing_name,Billing_name_locator)
time.sleep(5)
send_data(Billing_phone,Billing_phone_locator)
time.sleep(5)
send_data(Email_id,Email_id_locator)
time.sleep(5)
send_data(Street_Address,Street_Address_locator)
time.sleep(5)
element = get_element(Country_locator)   #(dropdown)
select_obj1 = Select(element)
time.sleep(5)
select_obj1.select_by_visible_text("Algeria")
# select_obj1.select_by_value("AX")
# select_obj1.select_by_index("5")
time.sleep(5)
send_data(Postal,Postal_Locator)
time.sleep(5)
send_data(prefecture,prefecture_locator)
time.sleep(5)
send_data(Street_add1,Street_add1_locator)
time.sleep(5)
send_data(Street_add2,Street_add2_locator)
time.sleep(5)

#Checkboxes scenario-Most visited cities
checkboxes = click_elements(most_visited_cities_locator)
print (len(checkboxes))