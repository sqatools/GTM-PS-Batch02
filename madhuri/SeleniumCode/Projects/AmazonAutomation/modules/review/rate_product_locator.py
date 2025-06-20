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

# New Your Order:
select_order_year_locator = (By.ID, "orderFilter")
product_review_locator = (By.XPATH, "//a[@id='Write-a-product-review_1']")
star_rating_locator = (By.XPATH, "(//button[@class='ryp__star__button'])[5]")
submit_review_btn_locator = (By.XPATH, "//span[@data-hook='ryp-review-submit-button']//button")