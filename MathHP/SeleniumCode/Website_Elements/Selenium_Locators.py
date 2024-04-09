from selenium.webdriver.common.by import By

############# POM Page Object Model #################

first_name_locator = (By.XPATH,"(//input[@id='firstname'])[1]")
last_name_locator = (By.XPATH, "(//input[@id='firstname'])[2]")

male_locator = (By.XPATH,"(//input[@id='male'])")
female_locator = (By.XPATH,"(//input[@id='female'])[1]")

from_city = (By.ID,"fromcity")
to_city = (By.ID,"destcity")