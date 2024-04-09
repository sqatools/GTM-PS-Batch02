import time

from selenium import  webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome()
wait = WebDriverWait(driver, 15, poll_frequency=1)
driver.maximize_window()
driver.get("https://automationbysqatools.blogspot.com/2021/05/dummy-website.html")
element = wait.until(ec.visibility_of_element_located((By.ID, "billing_country")))
select_obj = Select(element)
#select_obj.select_by_visible_text("Barbados")
#select_obj.select_by_value("AG")
select_obj.select_by_index(3)
time.sleep(5)

element_dd = wait.until(ec.visibility_of_element_located((By.ID, "admorepass")))
select_obj2 = Select(element_dd)
select_obj2.select_by_value("3")
time.sleep(5)

# select value from calender
date_element = wait.until(ec.visibility_of_element_located((By.ID, "birthday")))
date_element.send_keys("04/08/2024")
time.sleep(5)

depart_date = wait.until(ec.visibility_of_element_located((By.ID, "departdate")))
depart_date.send_keys("04/07/2025")

return_date = wait.until(ec.visibility_of_element_located((By.ID, "returndate")))
return_date.send_keys("04/09/2025")

time.sleep(5)
# Get attribute value

radio_element = wait.until(ec.visibility_of_element_located((By.XPATH, "(//li/input[@type='radio'])[2]")))
attrb_value = radio_element.get_attribute("value")
print("attribute value :", attrb_value)
time.sleep(5)

driver.close()



