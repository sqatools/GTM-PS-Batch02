from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(10)
driver.get("https://automationbysqatools.blogspot.com/2021/05/dummy-website.html")
driver.implicitly_wait(3)

#SQA tools
Logo= driver.find_element(By.XPATH, "//img[@alt = 'SQA Tools : Online Learning Platform']").text
print(f"Logo text: {Logo}")
driver.implicitly_wait(3)
#
driver.find_element(By.XPATH,"//h3[contains(text() ,'Dummy Website')]").text()

#Radio button main heading--Choose the correct option:
driver.find_elements(By.XPATH,"//div//h3[contains(text(), 'Choose the correct option:')]")
?? if i want to find the list of all elements in the main heading
#Radio button sub heading--
first_checkboxes = (By.XPATH, "//input[@type = 'radio']")
sub_heading = driver.find_element(By.XPATH,"//li//span[contains(text(),'Dummy hotel booking ticket - $400 ')]").text #third option
print(f"sub heading of radio button options:,{sub_heading}")

##Passenger Details
driver.find_element(By.XPATH,"//h2[contains(text() , 'Passenger Details')]").click()
driver.implicitly_wait(3)
#Firstname
Firstname= (By.XPATH,"//input[@id = 'firstname'][1]").send_keys("Neha")
driver.implicitly_wait(3)
#LastName
LastName= (By.XPATH,"//input[@id = 'firstname'][2]").send_keys("Kumari")
driver.implicitly_wait(3)
#DOB
DOB= (By.XPATH,"//input[@id = 'birthday']").click()
driver.implicitly_wait(3)
#Radio button-Sex
male_rdbtn= (By.XPATH,"//input[contains(@id , 'male')]").click() #for male radio button
driver.implicitly_wait(3)
female_rdbtn= (By.XPATH,"//span[contains(text(), 'Female')]").click() #for female radio button
driver.implicitly_wait(3)

#additional Passenger details
driver.find_element(By.XPATH,"//h3[contains(text() , 'Additional Passangers')]").click()
driver.implicitly_wait(3)
#Dropdown options
driver.find_element(By.XPATH,"//select//option[contains(text() , 'Add 2 more passenger')]").click()
#travel Details
Travel_details = driver.find_element(By.XPATH,"//h2[contains(text() , ' Travel Details ')]").text
print(f"Validation Travel details text: {Travel_details}")
driver.implicitly_wait(3)
#One way Radio button
driver.find_element(By.XPATH,"//input[@id = 'oneway']").click()
#Round trip
driver.find_element(By.XPATH,"//input[@id = 'Round Trip']").click()
#Delivery Details
driver.find_element.(By.XPATH,"//h2[contains (text(), 'Delivery Option')]")
#Visa Date (combination of preceding and following)
driver.find_element(By.XPATH,"//h2[contains (text(), 'Delivery Option')]//following::input[@id = 'whatsapp']//preceding::input[@name = 'visadate']").click()
#radio button
driver.find_element(By.XPATH,"//h2[text()='Billing Details']//preceding::input[@id='eamil']") ##preceding
driver.find_element(By.Xpath,"//h2[contains (text(), 'Delivery Option')]//following::input[@id = 'whatsapp']").click() ##following
driver.find_element(By.XPATH,"//span[contains(text(), 'Both')]")









