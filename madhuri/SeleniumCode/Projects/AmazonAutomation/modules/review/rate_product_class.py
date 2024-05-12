from base.selenium_base import SeleniumBase
from .rate_product_locator import *
import time


class ReviewProduct(SeleniumBase):
    def __init__(self, driver):
        super().__init__(driver)

    def open_login_page(self):
        self.move_to_element(home_page_signup_locator)
        self.click_to_element(sign_in_locator)
        time.sleep(3)

    def enter_username(self, username):
        self.enter_values(email_input_locator, username)

    def enter_password(self, password):
        self.enter_values(password_input_locator, password)

    def submit_username(self):
        self.click_element(submit_btn_locator)

    def submit_password(self):
        self.click_element(sign_in_final_submit_btn_locator)


# ------------------------------------ Function Start Here ------------------------------------------------#

    def login_user(self,
                   username: str,
                   password: str):
        self.open_login_page()
        self.enter_username(username)
        self.submit_username()
        time.sleep(3)
        self.enter_password(password)
        self.submit_password()
        time.sleep(2)

    def your_orders(self):
        """
        1. Go to your orders
        2. You have not placed any orders in past 3 months. View orders in 2024
        3. No order present -> click on View orders till it does not shows order list
        """
        # Go To Your Orders
        self.move_to_element(profile_edit_nav_locator)
        self.click_to_element(your_orders_nav_locator)
        time.sleep(3)

    def view_order_list(self):
        no_orders_text = self.get_text(no_of_orders_locator)
        no_orders_text_list = no_orders_text.split(" ")
        count = int(no_orders_text_list[0])

        test_count = 5
        while True:
            if count == 0 and test_count != 0:
                self.click_element(view_orders_by_year)
                time.sleep(1)

                # update repeat_count (no of time it should search)
                test_count = test_count - 1

                # update count
                no_orders_text = self.get_text(no_of_orders_locator)
                no_orders_text_list = no_orders_text.split(" ")
                count = int(no_orders_text_list[0])
            else:
                break

        time.sleep(2)

        no_orders_text = self.get_text(no_of_orders_locator)
        no_orders_text_list = no_orders_text.split(" ")
        count = int(no_orders_text_list[0])
        print(count)

        if count > 0:
            print('count greater than zero')
            print(write_product_review_locator)
            self.click_element(write_product_review_locator)

    def view_orders(self):
        self.your_orders()
        self.view_order_list()

    def provide_feedback(self):
        self.rate_by_star(overall_rating_locator, label='overall_rating', count=4)
        time.sleep(2)
        # Add condition here
        # if rating element visibile on page then only rate else not
        self.rate_by_star(night_vision_locator, label='night_vision', count=3)
        time.sleep(2)
        self.rate_by_star(value_for_money_locator, label='value_for_money', count=5)
        time.sleep(2)
        self.enter_values(review_title_locator, 'nice product')
        time.sleep(2)
        self.enter_values(review_text_card_locator, 'worth it')
        time.sleep(2)
        # self.click_element(submit_review_locator)
        time.sleep(2)