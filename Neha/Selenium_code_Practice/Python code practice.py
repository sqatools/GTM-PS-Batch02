from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
driver.maximize_window()
driver.implicitly_wait(10)
driver.find_element(By.NAME ,"username").send_keys("Admin")
driver.implicitly_wait(10)
driver.find_element(By.NAME, "password").send_keys("admin123")
driver.implicitly_wait(10)
driver.find_element(By.XPATH , '//button[@type="submit"]').click()
driver.implicitly_wait(10)

Actual_title = driver.title
driver.implicitly_wait(3)
Expected_title = "OrangeHRM"

if Actual_title == Expected_title:
    print(f"Logged In successfully")
else:
    print("logged In unsuccessfull")

# ##Admin Tab
# driver.implicitly_wait(3)
# driver.switch_to.frame("oxd-sidepanel")
# driver.switch_to.frame(driver.find_elements(By.TAG_NAME, "aside")[0])
# driver.implicitly_wait(3)
# Admin_tab= driver.find_element(By.CLASS_NAME,"oxd-text oxd-text--span oxd-main-menu-item--name").text
# print("Admin text :", Admin_tab)
# driver.implicitly_wait(3)
# #
# #     "dummy_sub_heading = driver.find_element(By.CLASS_NAME, "post-title").text
# #
# #
# # print("Sub heading text :", dummy_sub_heading)")
# #
# # driver.find_element(By.XPATH, "//button[@type ='button']").click()
# # driver.implicitly_wait(3)
# # driver.find_element(By.LINK_TEXT,"//span[contains(text(),'Admin']").click()
# # driver.implicitly_wait(3)
# # page_title = driver.find_element(By.TAG_NAME,"User Management").click()
# ##Fields
driver.find_element(By.XPATH,"//div//label[contains(text(), 'Username')]//following::div//input[@class='oxd-input oxd-input--active']").send_keys('NEHA')
driver.implicitly_wait(3)
# Userrole_dropdown = driver.find_element(By.XPATH, "//div[contains(text(),'-- Select --')][1]").text
# print("Sub heading text :", dummy_sub_heading)
# driver.find_element(By.XPATH,"//input[@placeholder = 'Type for hints...']").click()
# driver.implicitly_wait(3)
# search = driver.find_element(By.XPATH,"//button[@type = 'submit']")
# driver.implicitly_wait(3)
# search.click()


# #checkbox
# checkbox = driver.find_element(By.XPATH,"//div[contains(text(),'Admin1234')]//preceding::input[@type='checkbox' and @value = '1']").click()
# driver.close()
