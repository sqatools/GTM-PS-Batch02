from selenium.webdriver.common.by import By

# Home-Page
home_page_signup_locator = (By.XPATH, "//*[contains(text(),'Account & Lists')]")

# Sign-Up
start_here_text_locator = (By.XPATH, "(//div[@id='nav-flyout-accountList']//following::a[contains(text(), 'Start here')])[1]")

# Login-Page
sign_in_locator = (By.XPATH, "//span[contains(text(), 'Sign in')]")
email_input_locator = (By.ID, "ap_email")
submit_btn_locator = (By.XPATH, "//input[@id='continue']")
password_input_locator = (By.XPATH, "//input[@id='ap_password']")
sign_in_final_submit_btn_locator = (By.ID, "signInSubmit")
remember_me_locator = (By.XPATH, "//label//following::input[@name='rememberMe']")
send_otp_button_locator = (By.XPATH, "(//span[@class='a-button-inner']//input[@type='submit'])[2]")

# Create Account
verify_mobile_btn_locator = (By.XPATH, "//span[contains(text(),'Verify mobile number')]//preceding-sibling::input[@type='submit']")
customer_name_locator = (By.ID, "ap_customer_name")
phone_number_locator = (By.ID, "ap_phone_number")
password_locator = (By.ID, "ap_password")

# Home Page After Login - Rate your ordered product
profile_edit_nav_locator = (By.XPATH, "//span[@class='abnav-accountfor']//parent::span[@class='nav-line-2']")
your_orders_nav_locator = (By.XPATH, "//span[contains(text(),'Your Orders')]//parent::a")
no_of_orders_locator = (By.CLASS_NAME, "num-orders")
view_orders_by_year = (By.XPATH, "//div[contains(text(),' You have not placed any orders')] //following-sibling::a")
no = 1
write_product_review_locator = (By.ID, f"Write-a-product-review_{no}")

# Review Form
review_form = (By.CLASS_NAME, "ryp__review-form__form")
overall_rating_locator = (By.XPATH, "//span[contains(text(),'Rate features')]//preceding::button[@data-hook='ryp-star']")
night_vision_locator = (By.XPATH, "//span[contains(text(),'Night vision')]//following::button[@data-hook='ryp-star']")
value_for_money_locator = (By.XPATH, "//span[contains(text(),'Value for money')]//following::button[@data-hook='ryp-star']")
review_title_locator = (By.ID, "scarface-review-title-label")
review_text_card_locator = (By.ID, "scarface-review-text-card-title")
submit_review_locator = (By.XPATH, "//span[@data-hook='ryp-review-submit-button']//button")

# 5. Search product using its name in search bar
search_bar_locator = (By.ID, "twotabsearchtextbox")
search_icon_locator = (By.ID, "nav-search-submit-button")
# filter_by_category_locator = (By.XPATH, "//span[contains(text(),'Women's Running Shoes")]")
filter_by_price_locator = (By.XPATH, "//span[contains(text(),'Under ₹500')]")
# filter_by_color_locator = (By.XPATH, "")

