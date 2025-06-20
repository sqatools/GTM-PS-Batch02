from base.selenium_base import SeleniumBase
from utilities.get_logger import logger
from .search_product_locator import *
import time

log = logger

class SearchProduct(SeleniumBase):
    def __init__(self, driver):
        super().__init__(driver)

    def click_to_search_icon(self):
        self.click_element(search_icon_locator)

    def select_category(self, product_name):
        self.enter_values(search_bar_locator, product_name)

    def select_brand(self):
        self.click_element(filter_by_brand_locator)

    def select_price(self):
        self.click_element(filter_by_price_locator)

    def product_details(self):
        self.click_element(product_details_locator)

    def click_to_product(self):
        self.click_element(product_details_locator)

    def get_product_name(self):
        name = self.get_text(name_text_locator)
        log.info(f"Product Name : {name}")

    def get_product_price(self):
        price = self.get_text(price_text_locator)
        log.info(f"Product Price : {price}")

    def get_product_description(self):
        description = self.get_text(description_text_locator)
        log.info(f"Product Description : {description}")

    def get_product_review(self):
        review = self.get_text(reviews_text_locator)
        log.info(f"Product Review : {review}")

#     ------------------- cart --------------------
    def add_to_cart(self):
        self.click_element(add_to_cart_btn_locator)

    def verify_item_added_to_cart(self):
        item = self.get_element(item_added_to_cart_txt_locator)
        if item:
            log.info(f"item added to the cart", {item})
        else:
            log.info(f"item failed to add item cart")

    def go_to_cart(self):
        self.click_element(go_to_cart_locator)

    def select_quantity_to_buy_item(self, qty):
        self.select_dropdown(select_qanty_dropdown_locator, qty)

    def delete_item(self):
        del_ele = self.click_element(delete_item_locator)
        if del_ele:
            print("Found to delete")
        else:
            print("Not found to delete")

    def click_to_buy_item(self):
        self.click_element(buy_now_locator)
#     ----------------- select adddres and payment menthod-------------------

    def close_business_po_number(self):
        self.click_element(continue_business_order_info_locator)

    def get_address(self):
        address_line1 = self.get_text(deliver_address_line1_locator)
        address_line2 = self.get_text(deliver_address_line2_locator)
        address_line3 = self.get_text(deliver_address_line3_locator)
        address_line4 = self.get_text(deliver_address_line4_locator)
        if address_line1 and address_line2 and address_line3 and address_line4:
            log.info(f"address found")
        else:
            log.error(f"address not found")

    def get_payment(self):
        payment_element = self.get_element(payment_locator)
        if payment_element:
            print("pyment section found")
            log.info("pyment section found")
        else:
            log.error("pyment section not found")

    def get_order_summary(self):
        order_element = self.get_element(order_summary_locator)
        if order_element:
            print("order summary section found")
            log.info("order summary section found")
        else:
            log.error("order summary section not found")

    def select_payment(self):
        default_debit_card = self.click_element(default_debit_card_locator)
        credit_debit_card = self.click_element(credit_debit_card_locator)
        net_banking = self.click_element(net_banking_locator)
        other_upi_apps = self.click_element(other_upi_apps_locator)
        emi_apps = self.click_element(emi_apps_locator)
        cash_on_delivery_apps = self.click_element(cash_on_delivery_apps_locator)

    def submit_payment(self):
        print('click to payment')
        # self.click_element(payment_button_locator)

    def apply_coupon(self, coupon_code):
        self.enter_values(apply_coupon_code_locator, coupon_code)

    def submit_coupon_code(self):
        self.click_element(apply_coupon_code_btn_locator)

    # ------------------------------------ Function Start Here ------------------------------------------------#

    def search_product_with_filters(self, product_name):
        self.select_category(product_name)
        self.click_to_search_icon()
        time.sleep(2)
        self.select_brand()
        time.sleep(2)
        self.select_price()
        time.sleep(2)

    def show_product_details(self):
        self.click_to_product()
        self.windows_handle()
        time.sleep(10)
        self.get_product_name()
        self.get_product_price()
        self.get_product_description()
        self.get_product_review()
        time.sleep(10)

    def add_to_cart_item(self):
        self.add_to_cart()
        time.sleep(2)
        self.verify_item_added_to_cart()

    def update_item_quanty_cart(self, qty):
        self.go_to_cart()
        self.select_quantity_to_buy_item(qty)
        time.sleep(5)
        self.delete_item()
        time.sleep(5)
        self.switch_to_default_windows()

    def validate_checkout_process(self):
        self.click_to_product()
        self.windows_handle()
        time.sleep(10)
        self.click_to_buy_item()
        time.sleep(20)
        # self.get_address()
        # self.payment_method()
        # self.order_review()

    def validate_address_payment_process(self):
        self.close_business_po_number()
        self.get_address()
        self.get_payment()
        self.get_order_summary()

    def apply_coupon_code(self, coupon_code):
        self.apply_coupon(coupon_code)
        self.submit_coupon_code()
        time.sleep(5)

    def select_each_payment_method(self):
        self.select_payment()