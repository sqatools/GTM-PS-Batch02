from selenium.webdriver.common.by import By

#Radio button sub heading--
first_checkboxes = (By.XPATH, "//input[@type = 'radio']")


##Passenger Details
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

##Travel Details
Travel_details_locator = (By.XPATH,"//h2[contains(text() , ' Travel Details ')]")
#One way Radio button
Oneway_locator = (By.ID , 'oneway')
#Round trip
roundtrip_locator = (By.ID ,'roundtrip')
#Fromcity
fromcity_locator = (By.ID , "fromcity")
#destination City
destcity_locator = (By.ID , "destcity")

#Delivery details
Deliveryoption_locator = (By.XPATH,"//h2[contains (text(), 'Delivery Option')]")
#Visa Date (combination of preceding and following)
Visa_interview_locator = (By.XPATH,"//h2[contains (text(), 'Delivery Option')]//following::input[@id = 'whatsapp']//preceding::input[@name = 'visadate']")
#radio button for ticket receiving mode
Email_locator = (By.XPATH,"//h2[text()='Billing Details']//preceding::input[@id='eamil']")
whatsapp_locator = (By.XPATH,"//h2[contains (text(), 'Delivery Option')]//following::input[@id = 'whatsapp']")
Both_locator = (By.XPATH,"//span[contains(text(), 'Both')]")

#Billing Details

Billing_name_locator = (By.ID,"billing_name")
Billing_phone_locator = (By.ID,"billing_phone")
Email_id_locator = (By.ID, "billing_email")
Street_Address_locator = (By.ID,"billing_address")
Country_locator = (By.ID , "billing_country")
Postal_Locator = (By.ID,"postcode")
prefecture_locator = (By.ID,"Prefecture")
Street_add1_locator = (By.ID,"street_address1")
Street_add2_locator = (By.ID,"street_address2")
