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
# element screenshot
element_dd.screenshot("addmorepassenger.png")

# webpage screenshot
driver.save_screenshot("webpage.png")
driver.close()



