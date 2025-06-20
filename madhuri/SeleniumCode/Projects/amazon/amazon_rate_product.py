import time
from amazon_locator import *
from amazon_functions import *
from amazon_data import *

driver, wait = get_driver()

move_to_element(home_page_signup_locator)
click_to_element(sign_in_locator)
time.sleep(3)
# verify we are on registration page
login_page_title = driver.title
assert login_page_title == login_title

click_element(submit_btn_locator)
time.sleep(3)
send_data(email_input_locator,mobile_number)
time.sleep(3)
click_element(submit_btn_locator)
time.sleep(3)
send_data(password_input_locator, password)
time.sleep(3)
click_element(sign_in_final_submit_btn_locator)
time.sleep(15)
click_element(send_otp_button_locator)
time.sleep(5)

after_login_page_title = driver.title
print(after_login_page_title)
print(home_page_title)
# assert after_login_page_title == home_page_title
time.sleep(5)

# Go To Your Orders
move_to_element(profile_edit_nav_locator)
click_to_element(your_orders_nav_locator)
time.sleep(3)

no_orders_text = get_text(no_of_orders_locator)
print("Orders : ", no_orders_text)


# def check_product_order_list(count, no_of_pass=3):
#     print('recursion fun: ', count)
#     i = 0
#     while(i < no_of_pass):
#         if count == 0:
#             click_element(view_orders_by_year)
#             i = i + 1
#             print('click element', i)
#         else:
#             check_product_order_list(count)
#             i = i + 1
#             print('click element', i)
time.sleep(2)

no_orders_text_list = no_orders_text.split(" ")
count = int(no_orders_text_list[0])
if count == 0:
    click_element(view_orders_by_year)
    click_element(view_orders_by_year)

time.sleep(2)

no_orders_text = get_text(no_of_orders_locator)
no_orders_text_list = no_orders_text.split(" ")
count = int(no_orders_text_list[0])
print(count)

if count > 0:
    print('count greater than zero')
    print(write_product_review_locator)
    click_element(write_product_review_locator)


time.sleep(30)