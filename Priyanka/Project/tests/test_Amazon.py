import pytest
from data.Amazon_testdata import *
from data.session_data import *
from modules.Amazon_page_class import Amazon_modules

@pytest.mark.usefixtures("initiate_driver")
class TestcasesAmazon:

    @pytest.fixture(autouse=True)
    def setup(self):
        self.Amazon = Amazon_modules(self.driver)

    # 1. Test if new user can successfully register
    def test_new_user_registartion(self):
        self.Amazon.register_new_user(new_username=Amazon_data['new_username'],
                                     new_mobile=Amazon_data['new_mobile'],
                                      new_pw=Amazon_data['new_pw']
                                    )

    # 3. login fails with incorrect email or password
    def test_login_amazon_fail(self):
        self.Amazon.enter_incorrect_login_data(URL=URL,incorrect_email=Amazon_data['incorrect_email'])

    # 2. Verify login successful with correct email and Pw

    def test_login_amazon_successful(self):
        self.Amazon.enter_login_data(URL=URL,
                                     email=Amazon_data['email'],
                                     password=Amazon_data['password']
                                     )
    # 4. Check if user can edit profile info
    #def edit_profile_info(self):
    #    self.Amazon.(email=Amazon_data['incorrect_email'])
    
    # 5. Search for product using name like shoe
    def test_search_for_product_with_name(self):
        self.Amazon.search_for_product(URL, product_name=Amazon_data['product_name'])

    # 6. search with filters(e.g., category, price) yields accurate results
    def test_search_for_product_with_filters(self):
        self.Amazon.search_product_with_filters(category=Amazon_data['category'],
                                                brand=Amazon_data['brand'],
                                                price_range=Amazon_data['price_range'])

    # 7. Product details page display all necessary info(price, reviews, description)
    def test_product_details_page(self):
        self.Amazon.check_all_product_details()

    # 9. Verify that item can be added to the shopping cart
    def test_add_item_to_shopping_cart(self):
        self.Amazon.shopping_cart_add_item()

    # 10. Update item quantities and removing items from cart.
    def test_update_qty_and_remove_cart(self):
        self.Amazon.update_qty_remove_item_cart(qty=Amazon_data['qty'])
    
    
    # 11. Validate the entire check out process, including address section, payment method section, and order review.
    def test_validate_checkout_process(self):
        # self.Amazon.enter_login_data(URL=URL, email=Amazon_data['email'], password=Amazon_data['password'])
        self.Amazon.search_for_product(URL, product_name=Amazon_data['product_name'])
        self.Amazon.search_product_with_filters(category=Amazon_data['category'],
                                                brand=Amazon_data['brand'],
                                                price_range=Amazon_data['price_range'])

        self.Amazon.validate_checkout_process()

    # 12. check if user is able to select each payment method.
    def test_select_each_payment_method(self):
        self.Amazon.select_each_payment_method()


    # 13. check if user is able to apply for coupon code while ordering
    def test_apply_coupon_code(self):
        self.Amazon.check_user_apply_coupon_code()

    # 14. go to orders page anf give 5 star rating
    def test_go_to_orders_page_give_rating(self):
        self.Amazon.give_ratings(URL=URL)

    # 15. reach till cart page without login
    def test_reach_till_cart_without_login(self):
        #self.Amazon.enter_login_data(URL=URL, email=Amazon_data['email'], password=Amazon_data['password'])
        self.Amazon.search_for_product(URL, product_name=Amazon_data['product_name'])
        self.Amazon.search_product_with_filters(category=Amazon_data['category'],
                                                brand=Amazon_data['brand'],
                                                price_range=Amazon_data['price_range'])

        self.Amazon.check_all_product_details()
        self.Amazon.shopping_cart_add_item()





