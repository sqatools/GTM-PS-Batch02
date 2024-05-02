from base.selenium_base import SeleniumBase
from .search_product_locator import *
import time


class SearchProduct(SeleniumBase):
    def __init__(self, driver):
        super().__init__(driver)

    def enter_product_to_search(self, product_name):
        self.enter_values(search_bar_locator, product_name)

    def click_to_search(self):
        self.click_element(search_icon_locator)

    def filter_by_price(self):
        self.click_element(filter_by_price_locator)

    def product_details(self):
        self.click_element(product_details_locator)

# ------------------------------------ Function Start Here ------------------------------------------------#

    def search_product_by_name(self, product_name):
        self.enter_product_to_search(product_name)
        self.click_to_search()
        self.filter_by_price()
        self.product_details()
        time.sleep(5)



