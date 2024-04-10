from selenium.webdriver.common.by import By

first_name_locator = (By.XPATH, "(//12input[@id='firstname'])[1]")
last_name_locator = (By.XPATH, "(//input[@id='firstname'])[2]")
male_locator = (By.ID, "male")
female_locator = (By.ID, "female")
fromcity_locator = (By.ID, "fromcity")
destination_locator = (By.ID, "destcity")
header_locator = (By.XPATH, "//h1[@align='center']")
country_dropdown_locator = (By.ID, "billing_country")
add_more_pass_dd_locator = (By.ID, "admorepass")

