from selenium.webdriver.common.by import By

first_name_locator=(By.XPATH,"(//input[@id='firstname'])[1]")
last_name_locator=(By.XPATH,"(//input[@id='firstname'])[2]")
correct_option_locator = (By.XPATH, "//span[text()='Dummy ticket for visa application - $200 ']")
DOB_locator=(By.ID,"birthday")
gender_locator=(By.XPATH,"//span[text()='Male']")
from_city_locator=(By.ID,"fromcity")
dest_city_locator=(By.ID,"destcity")
departure_locator=(By.ID,"departdate")
return_locator=(By.ID,"returndate")
Visa_locator=(By.ID,"visadate")
Billing_loctor=(By.ID,"billing_name")
