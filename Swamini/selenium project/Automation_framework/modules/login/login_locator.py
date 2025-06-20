from selenium.webdriver.common.by import By


click_sign_in_locator= (By.ID,"nav-link-accountList-nav-line-1")
enteremail_locator=(By.ID,"ap_email")
click_continue_locator=(By.XPATH,"//input[@id='continue']")
enter_password_locator=(By.ID,"ap_password")
signin_locator=(By.ID,"signInSubmit")
incorrect_email_div_locator = (By.XPATH, "//div[@id='auth-error-message-box']//h4")
incorrect_email_pwd_msg_locator = (By.XPATH, "//div[@id='auth-error-message-box']//span")
amazon_logo_locator = (By.CLASS_NAME, "a-link-nav-icon")
