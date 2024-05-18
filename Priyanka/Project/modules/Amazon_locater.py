from selenium.webdriver.common.by import By

email_txtbox_loc = (By.XPATH, "//input[@name = 'email']")
continue_btn_loc = (By.XPATH, "//input[@id = 'continue']")
password_txtbox_loc = (By.XPATH, "//input[@name = 'password']")
signin_btn_loc = (By.ID, "signInSubmit")
navigate_signin_loc = (By.XPATH, "//a[@id='nav-link-accountList']")
create_new_btn_loc = (By.ID, "createAccountSubmit")
new_username_loc = (By.XPATH, "//input[@name='customerName']")
new_mobile_loc = (By.XPATH, "//input[@id='ap_phone_number']")
new_pw_loc = (By.XPATH, "//input[@id='ap_password']")
verify_mobile_no_btn_loc = (By.XPATH, "//input[@id='continue']")
incorrect_email_msg_loc = (By.XPATH, "//div[@id='auth-error-message-box']//span")
search_txtbox_loc = (By.XPATH, "//input[@id='twotabsearchtextbox']")
search_btn_loc = (By.ID, "nav-search-submit-button")
search_result_loc = (By.XPATH, "//span[@data-component-type='s-result-info-bar']//span[3]")
price_txt_loc = (By.XPATH, "//div[@id='apex_desktop']//span[@class='a-price-whole']")
description_txt_loc = (By.XPATH, "//div[@id='productDescription']//span")
reviews_txt_loc = (By.XPATH, "//span[@data-hook='rating-out-of-text']")
name_txt_loc = (By.XPATH, "//span[@id='productTitle']")
add_to_cart_btn_loc = (By.ID, "add-to-cart-button")
cart_txt_loc = (By.XPATH, "//div[@class='a-fixed-left-grid-inner']//h1[contains(text(),'Added to Cart')]")
product_link_loc = (By.XPATH, "(//div[@data-component-type='s-search-result']//img[@class='s-image'])[1]")
navigate_cart_loc = (By.XPATH, "//a[@id='nav-cart']")
quantity_dropdown_loc = (By.XPATH, "//select[@id='quantity']")
delete_link_loc = (By.XPATH, "//input[@value='Delete']")
buy_now_btn_loc = (By.XPATH, "//input[@id='buy-now-button']")
address_txt_loc = (By.XPATH, "//ul[@class='displayAddressUL']//li")
payment_loc = (By.XPATH, "//div[contains(@class, 'pay-desktop')]")
order_summary_loc = (By.XPATH, "//div[contains(@class, 'order-summary')]")
payment_method_radiobtn_loc = (By.XPATH, "//input[@name='ppw-instrumentRowSelection']")
payment_method_btn_loc = (By.XPATH, "//div[@class='a-fixed-left-grid']//span[text()='Use this payment method']//..//..//input")
claimCode_txt_box_loc = (By.XPATH, "//input[@name='claimCode']")
apply_btn_loc = (By.XPATH, "//span[@id='gcApplyButtonId']//input")
navigate_orders_loc = (By.XPATH, "//a[@id='nav-orders']")
time_filter_orders_loc = (By.XPATH, "//select[@id='time-filter']")
product_review_loc = (By.XPATH, "//a[@id='Write-a-product-review_2']")
rattings_loc = (By.XPATH, "(//button[@class='ryp__star__button'])[5]")


