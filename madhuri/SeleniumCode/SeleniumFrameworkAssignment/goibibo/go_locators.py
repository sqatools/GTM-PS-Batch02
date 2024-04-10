from selenium.webdriver.common.by import By

close_login_popup_locator = (By.CLASS_NAME, "logSprite")
one_way_trip_locator = (By.XPATH, "//ul/li//following-sibling::p")
from_input_locator = (By.XPATH, "//span[contains(text(),'From')]//following-sibling::input[@type='text']")
to_input_locator = (By.XPATH, "//span[contains(text(),'To')]//following-sibling::input[@type='text']")
