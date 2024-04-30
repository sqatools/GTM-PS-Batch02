
from selenium.webdriver.common.by import By

click_sign_in_locator= (By.ID,"nav-link-accountList-nav-line-1")
create_account_locator=(By.ID,"createAccountSubmit")
entername_locator=(By.ID,"ap_customer_name")
enter_mobno_locator=(By.ID,"ap_phone_number")
enter_password_locator=(By.ID,"ap_password")
click_continue_locator=(By.XPATH,"//input[@id='continue']")
click_startpuzzle=(By.XPATH,"//button[contains(text(),'Start Puzzle')]")

#2 Verify login is successful with correct email and passwor

enteremail_locator=(By.ID,"ap_email")
signin_locator=(By.ID,"signInSubmit")

#4 Check if a user can successfully edit their profile information.
click_profile_locator=(By.XPATH,"//a[contains(@href, 'manage-your-profiles')]")
profile_arrow_locator=(By.XPATH,"(//div[@class='a-column a-span11 a-spacing-base aok-break-word'])[1]")
click_pencilarrow_locator=(By.ID,"name-edit-pencil-image")
profilename_locator=(By.ID,"profile-name-text-input")
profile_save_locator=(By.ID,"profile-name-edit-submit-button")
profile_text_locator=(By.ID,"profile-name-section")

#5
search_locator=(By.ID,"twotabsearchtextbox")
clicksearch_locator=(By.ID,"nav-search-submit-button")