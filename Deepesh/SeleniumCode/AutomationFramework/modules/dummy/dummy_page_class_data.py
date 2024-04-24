from selenium.webdriver.common.by import By

first_name_locator = (By.XPATH, "(//input[@id='firstname'])[1]")
last_name_locator = (By.XPATH, "(//input[@id='firstname'])[2]")
dob_locator = (By.ID, "birthday")
male_locator = (By.ID, "male")
from_city_locator = (By.ID, "fromcity")
dest_city_locator = (By.ID, "destcity")

billing_name_locator = (By.ID, "billing_name")
billing_phone_locator = (By.ID, "billing_phone")
billing_email_locator = (By.ID, "billing_email")
billing_address_locator = (By.ID, "billing_address")
postcode_locator = (By.ID, "postcode")
prefecture_locator = (By.ID, "Prefecture")
street_address1_locator = (By.ID, "street_address1")
street_address2_locator = (By.ID, "street_address2")


