import time

import pytest
from data.search_product_data import *
from modules.search_product.search_product import SearchProduct


@pytest.mark.usefixtures("initiate_driver")
class TestSearchProduct:

    @pytest.fixture(autouse=True)
    def setup(self):
        self.sp = SearchProduct(self.driver)

    def test_search_product(self):
        self.sp.search_product_by_name(
            product_name=product_name,
        )




