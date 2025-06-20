from selenium.webdriver.common.by import By
# Home-Page
home_page_signup_locator = (By.XPATH, "//*[contains(text(),'Account & Lists')]")

# Login-Page
sign_in_locator = (By.XPATH, "//span[contains(text(), 'Sign in')]")
email_input_locator = (By.ID, "ap_email")
submit_btn_locator = (By.XPATH, "//input[@id='continue']")
password_input_locator = (By.XPATH, "//input[@id='ap_password']")
sign_in_final_submit_btn_locator = (By.ID, "signInSubmit")
remember_me_locator = (By.XPATH, "//label//following::input[@name='rememberMe']")
send_otp_button_locator = (By.XPATH, "(//span[@class='a-button-inner']//input[@type='submit'])[2]")
incorrect_email_div_locator = (By.XPATH, "//div[@id='auth-error-message-box']//h4")
incorrect_email_pwd_msg_locator = (By.XPATH, "//div[@id='auth-error-message-box']//span")
amazon_logo_locator = (By.CLASS_NAME, "a-link-nav-icon")


