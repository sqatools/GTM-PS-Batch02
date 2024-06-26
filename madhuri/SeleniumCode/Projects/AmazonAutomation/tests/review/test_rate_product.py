import time
import pytest
from data.amazon_data import *
from modules.review.rate_product_class import ReviewProduct
from modules.login.login_class import Login

@pytest.mark.usefixtures("initiate_driver")
class TestReviewProduct:

    @pytest.fixture(autouse=True)
    def setup(self):
        self.rp = ReviewProduct(self.driver)
        self.lg = Login(self.driver)

    def test_login_before_edit(self):
        self.lg.login_user(
            username=amazon_test_data['login']['correct_mobile'],
            password=amazon_test_data['login']['correct_password']
        )
        assert self.driver.title == amazon_test_data['page_title']['home_page_title']

    # def test_login_user(self):
    #     self.rp.login_user(
    #         username= amazon_test_data['login']['correct_mobile'],
    #         password= amazon_test_data['login']['correct_password']
    #     )
    #     assert self.driver.title == amazon_test_data['page_title']['home_page_title']

    # def test_view_orders(self):
    #     self.rp.view_orders()
    #     time.sleep(5)
    #
    # def test_provide_feedback(self):
    #     self.rp.provide_feedback()
    #     time.sleep(5)

    def test_give_rating_past_order(self):
        self.rp.give_rating(
            order_year = amazon_test_data['review']['year']
        )







