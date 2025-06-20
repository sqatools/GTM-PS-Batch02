import time

from selenium import  webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.alert import Alert

driver = webdriver.Chrome()
wait = WebDriverWait(driver, 15, poll_frequency=1)
driver.maximize_window()
driver.get("https://www.globalsqa.com/demo-site/frames-and-windows/#iFrame")

iframe_element = wait.until(ec.visibility_of_element_located((By.NAME, "globalSqa")))
driver.switch_to.frame(iframe_element)

phone_element = wait.until(ec.visibility_of_element_located((By.XPATH, "//div[@class='header_phone']")))
print("Phone_number :", phone_element.text)

email_element = wait.until(ec.visibility_of_element_located((By.XPATH, "//div[@class='header_mail']")))
print("Email ID :", email_element.text)

menu_element = wait.until(ec.visibility_of_element_located((By.ID, "mobile_menu_toggler")))
menu_element.click()

time.sleep(3)
sheet_element = wait.until(ec.visibility_of_element_located((By.LINK_TEXT, "CheatSheets")))
#sheet_element.click()
time.sleep(3)

# moving out of iframe, to concentrate on other content of website.
driver.switch_to.default_content()

header_element = wait.until(ec.visibility_of_element_located((By.XPATH, "//div[@class='page_heading']/h1")))
print("Website Header :", header_element.text)



driver.close()

