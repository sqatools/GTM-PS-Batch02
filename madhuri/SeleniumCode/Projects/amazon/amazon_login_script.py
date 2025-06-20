import time
from amazon_locator import *
from amazon_functions import *
from amazon_data import *

driver, wait = get_driver()


def login_user():
    move_to_element(home_page_signup_locator)
    click_to_element(sign_in_locator)
    time.sleep(3)

    # verify we are on registration page
    login_page_title = driver.title
    assert login_page_title == login_title

    click_element(submit_btn_locator)
    time.sleep(3)
    send_data(email_input_locator, mobile_number)
    time.sleep(3)
    click_element(submit_btn_locator)
    time.sleep(3)
    send_data(password_input_locator, password)
    time.sleep(3)
    click_element(sign_in_final_submit_btn_locator)

    # OTP Before Login
    # time.sleep(20)
    # click_element(send_otp_button_locator)
    # time.sleep(5)

    after_login_page_title = driver.title
    print('after login page title: ', after_login_page_title)
    print('home page title: ', home_page_title)
    assert after_login_page_title == home_page_title
    time.sleep(5)


login_user()

# Go To Your Orders
move_to_element(profile_edit_nav_locator)
click_to_element(your_orders_nav_locator)
time.sleep(3)

no_orders_text = get_text(no_of_orders_locator)
no_orders_text_list = no_orders_text.split(" ")
count = int(no_orders_text_list[0])

test_count = 5
while True:
    if count == 0 and test_count != 0:
        click_element(view_orders_by_year)
        time.sleep(1)

        # update repeat_count (no of time it should search)
        test_count = test_count - 1

        # update count
        no_orders_text = get_text(no_of_orders_locator)
        no_orders_text_list = no_orders_text.split(" ")
        count = int(no_orders_text_list[0])
    else:
        break

time.sleep(2)

no_orders_text = get_text(no_of_orders_locator)
no_orders_text_list = no_orders_text.split(" ")
count = int(no_orders_text_list[0])
print(count)

if count > 0:
    print('count greater than zero')
    print(write_product_review_locator)
    click_element(write_product_review_locator)

# Review Page
rate_by_star(overall_rating_locator, label='overall_rating', count = 4)
rate_by_star(night_vision_locator, label='night_vision', count = 3)
rate_by_star(value_for_money_locator, label='value_for_money', count = 5)
send_data(review_title_locator,'nice product')
send_data(review_text_card_locator, 'worth it')
click_element(submit_review_locator)

time.sleep(15)
driver.quit()