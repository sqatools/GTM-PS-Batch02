import time
from selenium import webdriver
from selenium.webdriver.common.by import By

URL = "https://automationbysqatools.blogspot.com/p/home.html"

driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(10)
driver.get(URL)

title = driver.title
print('title of website:', title)

driver.find_element(By.XPATH, "//div[contains(text(),'Dummy Website')]//parent::a").click()

# dummy website home page

driver.find_elements(By.XPATH, "//body//div[@class='body-fauxcolumns']")
# driver.save_screenshot("dummyweb.png")

# get title to page
page2_title = driver.title
print('title of dummy page:', page2_title)

# get current url of the page
print("Get the current url of the page: ", driver.current_url)

# verify page heading is correct
expected_header_text = 'Dummy Website'
header_text = driver.find_element(By.XPATH, "//h3[contains(text(),'Dummy Website')]").text
assert expected_header_text == header_text

# verify subheader text is correct or not
expected_subheader_text = 'Dummy Ticket Booking Website'
subheader_text = driver.find_element(By.XPATH, "//h1[contains(text(),'Dummy Ticket Booking Website')]").text
assert expected_subheader_text == subheader_text

# //input[@type='radio']//parent::li//ancestor::ul
# radio_element = driver.find_elements(By.XPATH, "//input[@type='radio']")
radio_element = driver.find_elements(By.XPATH, "//input[@type='radio']")

# //parent::li
print(radio_element)
print(len(radio_element))

for element in radio_element:
    radio_value = element.get_attribute("value")
    print('attr value: ', radio_value)
    if radio_value == 'radio_123':
        element.click()
        print("is selected: ", element.is_selected())
        break


time.sleep(5)
driver.close()

# one liner framewrk
# data driven framework
# page object model : hybrid model :integrating locator
# driven frame wrk:robot driven