import time
from selenium import webdriver
from selenium.webdriver.common.by import By

URL="https://automationbysqatools.blogspot.com/2021/05/dummy-website.html"

driver=webdriver.Chrome()
driver.maximize_window()
driver.get(URL)
#driver.find_element(By.XPATH,"//input[@type='checkbox']").click()
time.sleep(2)

driver.find_element(By.XPATH, "//span[text()='Dummy ticket for visa application - $200 ']").click()


# ID # Done
# XPATH #
# LINK_TEXT # Done
# PARTIAL_LINK_TEXT # Done
# NAME  # Done
# TAG_NAME # DONE   # IT slight difficult to find unique tag name on the webpage
# CLASS_NAME # Done
# CSS_SELECTOR

# #ID
# driver.find_element(By.ID,"firstname").send_keys("Arun")
# time.sleep(2)

#Xpath


#1)>Basic Xpath://tagname[@attribute='value']>>>Basic Xpath

#driver.find_element(By.XPATH,"//input[@name='firstname']").send_keys("Kumar")
time.sleep(2)

#2)Text Method :  //tagname[text()='text value']
#driver.find_element(By.XPATH,"//a[text()='Home']").click()
time.sleep(10)

#3)contains method: //tagname[contains(@attiribute,'value')]
driver.find_element(By.XPATH,"//input[contains(@name,'visadate')]").send_keys("10/10/1996")
time.sleep(2)

#4)Indexing : (// a[@ href= '/hotels/'])[1]
driver.find_element(By.XPATH,"//input[@id='firstname'][1]").send_keys("HI")
time.sleep(10)

