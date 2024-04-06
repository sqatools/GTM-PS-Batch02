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
