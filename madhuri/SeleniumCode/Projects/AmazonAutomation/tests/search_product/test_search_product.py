import time

import pytest
from data.amazon_data import *
from data.search_product_data import *
from modules.search_product.search_product import SearchProduct


@pytest.mark.usefixtures("initiate_driver")
class TestSearchProduct:

    @pytest.fixture(autouse=True)
    def setup(self):
        self.sp = SearchProduct(self.driver)

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

    def test_validate_checkout_process(self):
        self.sp.validate_checkout_process()