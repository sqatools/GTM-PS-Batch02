import time

import pytest
from data.review_page_data import *
from modules.review.rate_product_class import ReviewProduct


@pytest.mark.usefixtures("initiate_driver")
class TestReviewProduct:

    @pytest.fixture(autouse=True)
    def setup(self):
        self.rp = ReviewProduct(self.driver)

    def test_login_user(self):
        self.rp.login_user(
            username=mobile_number,
            password=password
        )
        # assert self.driver.title == home_page_title
        # self.rp.view_orders()

    def test_login_success(self):
        # assert self.driver.title == login_title  #failed test case
        assert self.driver.title == home_page_title
        time.sleep(2)

    def test_view_orders(self):
        self.rp.view_orders()
        time.sleep(5)

    def test_provide_feedback(self):
        self.rp.provide_feedback()
        time.sleep(5)







