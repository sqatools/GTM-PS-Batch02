from selenium.webdriver.common.by import By

profile_name_locator = (By.CLASS_NAME, "abnav-accountfor")
your_account_nav_locator = (By.XPATH, "//span[contains(text(),'Your Account')]//parent::a")
your_address_locator = (By.XPATH, "//article[@data-card-identifier='Addresses']")
edit_address_locator = (By.ID, "ya-myab-address-edit-btn-1")
edit_full_name_locator = (By.ID, "address-ui-widgets-enterAddressFullName")
submit_profile_locator = (By.XPATH, "span[@id='address-ui-widgets-form-submit-button-announce']//preceding-sibling::input")

