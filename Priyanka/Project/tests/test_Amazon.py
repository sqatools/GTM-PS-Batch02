import pytest
from data.Amazon_testdata import *
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

    # 2. Verify login successful with correct email and Pw
    def test_login_amazon_successful(self):
        self.Amazon.enter_login_data(email=Amazon_data['email'],
                                     passwoed=Amazon_data['password']
                                    )

    # 3. login fails with incorrect email or password
    def login_amazon_fail(self):
        self.Amazon.enter_incorrect_login_data(email=Amazon_data['incorrect_email'])

    # 4. Check if user can edit profile info
    #def edit_profile_info(self):
    #    self.Amazon.(email=Amazon_data['incorrect_email'])

    # 5. Search for product using name like shoe
    def search_for_product_with_name(self):
        self.Amazon.search_for_product(product_name=Amazon_data['product_name'])

    # 6. search with filters(e.g., category, price) yields accurate results
    def search_for_product_with_filters(self):
        self.Amazon.search_product_with_filters(category=Amazon_data['category'],
                                                brand=Amazon_data['brand'],
                                                price_range=Amazon_data['price_range'])

    # 7. Product details page display all necessary info(price, reviews, description)
    def product_details_page(self):
        self.Amazon.check_all_product_details()

    # 9. Verify that item can be added to the shopping cart
    def add_item_to_shopping_cart(self):
        self.Amazon.shopping_cart_add_item()


