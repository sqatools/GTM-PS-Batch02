from selenium.webdriver.common.by import By
# Home Page
home_page_signup_locator = (By.XPATH, "//*[contains(text(),'Account & Lists')]")
start_here_text_locator = (By.XPATH, "(//div[@id='nav-flyout-accountList']//following::a[contains(text(), 'Start here')])[1]")

# sign_in_register_nav_locator = (By.XPATH, "(//a[@data-nav-ref='nav_ya_signin']//following::span[@class='nav-icon nav-arrow'])[1]")


# Create Account
verify_mobile_btn_locator = (By.XPATH, "//span[contains(text(),'Verify mobile number')]//preceding-sibling::input[@type='submit']")
customer_name_locator = (By.ID, "ap_customer_name")
phone_number_locator = (By.ID, "ap_phone_number")
password_locator = (By.ID, "ap_password")
