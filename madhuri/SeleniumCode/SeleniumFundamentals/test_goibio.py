import time
from selenium import webdriver
from selenium.webdriver.common.by import By

URL = "https://www.goibibo.com/"

driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(10)
driver.get(URL)

driver.find_element(By.CLASS_NAME, "logSprite").click()
time.sleep(2)
# driver.find_element(By.XPATH, "//span[contains(text(),'From')]//following-sibling::input[@type='text']").send_keys('Mumbai')
# driver.find_element(By.XPATH, "//span[contains(text(),'To')]//following-sibling::input[@type='text']").send_keys('Pune')
radio_elements = driver.find_elements(By.XPATH, "//div//input[@name='speacialFare']")

for element in radio_elements:
    radio_value = element.get_attribute("value")
    # print(radio_value)
    # element.click()
    # print("is selected: ", element.is_selected())
