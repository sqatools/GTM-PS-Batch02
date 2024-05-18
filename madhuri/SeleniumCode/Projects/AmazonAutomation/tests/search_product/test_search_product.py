import time

import pytest
from data.amazon_data import *
from data.search_product_data import *
from modules.search_product.search_product import SearchProduct
from modules.login.login_class import Login

@pytest.mark.usefixtures("initiate_driver")
class TestSearchProduct:

    @pytest.fixture(autouse=True)
    def setup(self):
        self.sp = SearchProduct(self.driver)
        self.lg = Login(self.driver)

    def test_search_product(self):
        self.sp.search_product_with_filters(
            product_name=amazon_test_data['search']['product_name']
        )
        time.sleep(5)

    def test_show_product_details(self):
        self.sp.show_product_details()
        time.sleep(5)

    def test_add_to_cart_item(self):
        self.sp.add_to_cart_item()
        time.sleep(5)

    def test_update_item_quanty_cart(self):
        self.sp.update_item_quanty_cart(qty=amazon_test_data['search']['qty'])
        time.sleep(5)

    # 11. Validate the entire check out process, including address section, payment method section, and order review.
    def test_validate_checkout_process(self):
        self.sp.validate_checkout_process()
        assert self.driver.title == amazon_test_data['page_title']['login_title']
        self.lg.payment_login(
            correct_username=amazon_test_data['login']['correct_mobile'],
            correct_password=amazon_test_data['login']['correct_password']
        )
        # time.sleep(5)
        # assert self.driver.title == amazon_test_data['page_title']['checkout_page_title']
        self.sp.validate_address_payment_process()

    def test_apply_coupon_code(self):
        self.sp.apply_coupon_code(
            coupon_code=amazon_test_data['payment']['coupon']
        )

    def test_select_each_payment_method(self):
        self.sp.select_each_payment_method()