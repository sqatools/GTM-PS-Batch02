from selenium.webdriver.common.by import By

# Ticket Booking Options
choose_ticket_option_locator = (By.XPATH, "//li//input[@type = 'radio']")

# Passenger Details
passenger_heading_locator = (By.XPATH, "//h2[contains(text(), 'Passenger Details')]")
first_name_locator = (By.XPATH, "(//input[@id='firstname'])[1]")
dob_locator = (By.ID, "birthday")
last_name_locator = (By.XPATH, "(//input[@id='firstname'])[2]")
male_locator = (By.ID, "male")
female_locator = (By.ID, "female")

# Number of Additional Passangers
traveler_dropdown_locator = (By.ID, "admorepass")

# Travel Details
traveldetails_heading_locator = (By.XPATH, "//h2[contains(text(), 'Travel Details')]")
oneway_trip_locator = (By.ID, "oneway")
round_trip_locator = (By.ID,"roundtrip")
source_city_locator = (By.ID, "fromcity")
destination_city_locator = (By.ID, "destcity")
departdate_locator = (By.ID, "departdate")
returndate_locator = (By.ID, "returndate")


# Delivery Option
visadate_locator = (By.ID, "visadate")
deliveryoption_heading_locator = (By.XPATH, "//h2[contains(text(), 'Delivery Option')]")
ticket_by_email_locator = (By.ID, "eamil")
ticket_by_whatsapp_locator = (By.ID, "whatsapp")
ticket_by_both_locator = (By.ID, "//span[contains(text(), 'Both')]")

# Billing Locators
billing_heading_locator = (By.XPATH, "//h2[contains(text(), 'Billing Details')]")
billing_name_locator = (By.ID, "billing_name")
billing_phone_locator = (By.ID, "billing_phone")
billing_email_locator = (By.ID, "billing_email")
billing_address_locator = (By.ID, "billing_address")
billing_country_locator = (By.ID, "billing_country")
billing_postcode_locator = (By.ID, "postcode")
billing_prefecture_locator = (By.ID, "Prefecture")
billing_street_address1_locator = (By.ID, "street_address1")
billing_street_address2_locator = (By.ID, "street_address2")

# Most Visited Cities
cities_checkbox_options_locator = (By.XPATH, "//table//input[@type='checkbox']")









