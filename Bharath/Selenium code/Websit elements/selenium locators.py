from selenium.webdriver.common.by import By

first_name_locator = (By.XPATH, "(//input[@id='firstname'])[1]")
last_name_locator = (By.XPATH, "(//input[@id='firstname'])[2]")
male_locator = (By.ID, "male")
female_locator = (By.ID, "female")
fromcity_locator = (By.ID, "fromcity")
destination_locator = (By.ID, "destcity")
