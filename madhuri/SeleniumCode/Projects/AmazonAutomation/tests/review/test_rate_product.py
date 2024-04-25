import pytest
from modules.review.rate_product_class import ReviewProduct
from data.review_page_data import *


@pytest.mark.usefixtures("initiate_driver")
class TestReviewProduct:
    @pytest.fixture(autouse=True)
    def setup(self):
        self.rp = ReviewProduct(self.driver)

    def test_login_user(self):
        self.rp.login_user(
            username=mobile_number
        )




