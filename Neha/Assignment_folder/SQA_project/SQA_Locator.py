from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

# Ticket Booking Options
choose_ticket_option_locator = (By.XPATH, "//li//input[@type = 'radio']")


##Passenger Details
passenger_heading_locator = (By.XPATH, "//h2[contains(text(), 'Passenger Details')]")
#Firstname
Firstname_locator = (By.XPATH,"//input[@id = 'firstname'][1]")
#LastName
LastName_locator = (By.XPATH,"//input[@id = 'firstname'][2]")
#DOB
DOB_locator = (By.XPATH,"//input[@id = 'birthday']")
#Radio button-Sex
#for male radio button
male_rdbtn_locator = (By.XPATH,"//input[contains(@id , 'male')]")
#for female radio button
female_rdbtn_locator = (By.XPATH,"//span[contains(text(), 'Female')]")

#additional passenger details
dropdown_locator = (By.ID ,"admorepass")

##Travel Details

Travel_details_heading_locator = (By.XPATH,"//h2[contains(text() , ' Travel Details ')]")
#One way Radio button
Oneway_locator = (By.ID , 'oneway')
#Round trip
roundtrip_locator = (By.ID ,'roundtrip')
#Fromcity
fromcity_locator = (By.ID , "fromcity")
#destination City
destcity_locator = (By.ID , "destcity")

#Delivery details
delivery_option_heading_locator = (By.XPATH, "//h2[contains(text(), 'Delivery Option')]")

#Visa Date (combination of preceding and following)
Visa_interview_locator = (By.XPATH,"//h2[contains (text(), 'Delivery Option')]//following::input[@id = 'whatsapp']//preceding::input[@name = 'visadate']")
#radio button for ticket receiving mode
Email_locator = (By.XPATH,"//h2[text()='Billing Details']//preceding::input[@id='eamil']")
whatsapp_locator = (By.XPATH,"//h2[contains (text(), 'Delivery Option')]//following::input[@id = 'whatsapp']")
Both_locator = (By.XPATH,"//span[contains(text(), 'Both')]")

#Billing Details
billing_option_heading_locator = (By.XPATH, "//h2[contains(text(), 'Billing Details')]")
Billing_name_locator = (By.ID,"billing_name")
Billing_phone_locator = (By.ID,"billing_phone")
Email_id_locator = (By.ID, "billing_email")
Street_Address_locator = (By.ID,"billing_address")
Country_locator = (By.ID , "billing_country")
Postal_Locator = (By.ID,"postcode")
prefecture_locator = (By.ID,"Prefecture")
Street_add1_locator = (By.ID,"street_address1")
Street_add2_locator = (By.ID,"street_address2")

#Most visited cities

most_visited_cities_locator = (By.XPATH, "//table//input[@type='checkbox']")
