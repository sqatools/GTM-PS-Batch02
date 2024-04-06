import time

from SQA_Locator import *
from functions_file import *
from Testdata_file import *




get_driver(web_URL ,'Chrome',timeout=35)
send_data(Firstname, Firstname_locator)
send_data(LastName, LastName_locator)
time.sleep(5)
send_data(DOB, DOB_locator)
click_element(male_rdbtn_locator)
click_element(female_rdbtn_locator)

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
