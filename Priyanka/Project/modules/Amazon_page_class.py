from base.base_functions import SeleniumBase
from .Amazon_locater import *
from utilities.get_logger import logger
import time
log = logger


class Amazon_modules(SeleniumBase):

    def __init__(self, driver):
        super().__init__(driver)

    def navigate_to_signin(self):
        self.click_element(navigate_signin_loc)

    def create_new_account(self):
        self.click_element(create_new_btn_loc)

    def enter_new_name(self, new_username):
        self.enter_value(new_username_loc, new_username)

    def enter_new_phone(self, new_mobile):
        self.enter_value(new_mobile_loc, new_mobile)

    def enter_new_password(self, new_pw):
        self.enter_value(new_pw_loc, new_pw)

    def click_verify_mobile_no(self):
        self.click_element(verify_mobile_no_btn_loc)

    def enter_email(self, email):
        self.enter_value(email_txtbox_loc, email)

    def click_continue(self):
        self.click_element(continue_btn_loc)

    def enter_password(self, password):
        self.enter_value(password_txtbox_loc, password)

    def click_signin(self):
        self.click_element(signin_btn_loc)

    def varify_incorrect_email_error_msg(self):
        ele_txt = self.get_text(incorrect_email_msg_loc)
        try:
            if ele_txt == "We cannot find an account with that email address":
                log.info(f"Error message displayed: {ele_txt}")
            else:
                log.error(f"Error message not displayed: {ele_txt}")

        except Exception as e:
            log.info(f"Error message not displayed: {e}")
            raise

    def enter_product_name_and_search(self, product_name):
        self.enter_value(search_txtbox_loc, product_name)
        self.click_element(search_btn_loc)

    def varify_search_result(self, product_name):
        ele_txt = self.get_text(search_result_loc)
        if ele_txt == product_name:
            log.info(f"Product search successful: {ele_txt}")
        else:
            log.error(f"Product search failed: {ele_txt}")

    def choose_category(self, category):
        self.click_element((By.XPATH, "//div[@id='departments']//span[text()='"+category+"']"))


    def choose_brand(self, brand):
        #self.click_element(("//span[text()='"+brand+"']//..//..//input[@type='checkbox'"))
        self.click_element((By.XPATH, "//span[@class='a-list-item']//span[text()='"+brand+"']"))

    def choose_price_range(self, price_range):
        self.click_element((By.XPATH, "//a//span[text()='"+price_range+"']"))

    def get_price(self):
        price = self.get_text(price_txt_loc)
        log.info(f"Product Price : {price}")

    def get_description(self):
        description = self.get_text(description_txt_loc)
        log.info(f"Product Description : {description}")

    def get_review(self):
        review = self.get_text(reviews_txt_loc)
        log.info(f"Product Review : {review}")

    def get_name(self):
        name = self.get_text(name_txt_loc)
        log.info(f"Product Name : {name}")

    def click_add_to_cart(self):
        self.click_element(add_to_cart_btn_loc)

    def verify_item_added_to_cart(self):
        element = self.get_element(cart_txt_loc)
        if element:
            log.info("Item added to cart successfully")
        else:
            log.error("Item not added to cart")

    def click_on_product(self):
        self.click_element(product_link_loc)
        time.sleep(10)

    def go_to_cart(self):
        self.click_element(navigate_cart_loc)

    def select_qty(self, value):
        self.select_value_from_dropdown(quantity_dropdown_loc,value)

    def delete_item(self):
        self.click_element(delete_link_loc)

    def click_buy_now(self):
        self.click_element(buy_now_btn_loc)

    def get_address(self):
        #elements = self.get_elements(address_txt_loc)
        """for i in range(3):
            ele_text = self.get_text((By.XPATH, "//ul[@class='displayAddressUL']//li["+str(i)+"]"))
            print(ele_text)
            log.info(ele_text)"""
        ele_text1 = self.get_text((By.XPATH, "//ul[@class='displayAddressUL']//li[1]"))
        print(ele_text1)
        ele_text2 = self.get_text((By.XPATH, "//ul[@class='displayAddressUL']//li[2]"))
        print(ele_text2)
        ele_text3 = self.get_text((By.XPATH, "//ul[@class='displayAddressUL']//li[3]"))
        print(ele_text3)

    def payment_method(self):
        element = self.get_element(payment_loc)
        if element:
            print("pyment section found")
            log.info("pyment section found")
        else:
            log.error("pyment section not found")

    def order_review(self):
        element = self.get_element(order_summary_loc)
        if element:
            print("order summary section found")
            log.info("order summary section found")
        else:
            log.error("order summary section not found")

    def click_payment_radio_btn(self):
        """elements = self.get_elements(payment_method_radiobtn_loc)
        for ele in elements:
            ele.click()
        """
        self.click_element((By.XPATH, "(//input[@ name='ppw-instrumentRowSelection'])[1]"))
        self.click_element((By.XPATH, "(//input[@ name='ppw-instrumentRowSelection'])[2]"))
        self.click_element((By.XPATH, "(//input[@ name='ppw-instrumentRowSelection'])[3]"))
        self.click_element((By.XPATH, "(//input[@ name='ppw-instrumentRowSelection'])[4]"))
        self.click_element((By.XPATH, "(//input[@ name='ppw-instrumentRowSelection'])[5]"))

    def click_use_payment_btn(self):
        self.click_element(payment_method_btn_loc)

    def enter_coupon_code(self):
        self.enter_value(claimCode_txt_box_loc, "123456")

    def click_apply_btn(self):
        self.click_element(apply_btn_loc)

    def click_on_orders(self):
        self.click_element(navigate_orders_loc)

    def select_order_year(self):
        self.select_value_from_dropdown(time_filter_orders_loc, "2023")

    def click_Write_product_review(self):
        self.click_element(product_review_loc)

    def click_ratings(self):
        self.click_element(rattings_loc)

#------------------------------------------------------------------------------
    def register_new_user(self, new_username, new_mobile, new_pw):
        self.navigate_to_signin()
        self.create_new_account()
        self.enter_new_name(new_username)
        self.enter_new_phone(new_mobile)
        self.enter_new_password(new_pw)
        self.click_verify_mobile_no()
        time.sleep(10)


    def enter_login_data(self, URL, email, password):
        self.driver.get(URL)
        self.navigate_to_signin()
        self.enter_email(email)
        self.click_continue()
        self.enter_password(password)
        self.click_signin()
        time.sleep(30)

    def enter_incorrect_login_data(self, URL, incorrect_email):
        self.driver.get(URL)
        self.navigate_to_signin()
        self.enter_email(incorrect_email)
        self.click_continue()
        self.varify_incorrect_email_error_msg()
        time.sleep(10)

    def search_for_product(self, URL, product_name):
        self.driver.get(URL)
        self.enter_product_name_and_search(product_name)
        self.varify_search_result(product_name)
        time.sleep(10)

    def search_product_with_filters(self, category, brand, price_range):
        self.choose_category(category)
        time.sleep(5)
        self.choose_brand(brand)
        time.sleep(5)
        self.choose_price_range(price_range)
        time.sleep(5)

    def check_all_product_details(self):
        self.click_on_product()
        self.windows_handle()
        time.sleep(10)
        self.get_name()
        self.get_price()
        self.get_description()
        self.get_review()
        time.sleep(10)

    def shopping_cart_add_item(self):
        self.click_add_to_cart()
        self.verify_item_added_to_cart()

    def update_qty_remove_item_cart(self, qty):
        self.go_to_cart()
        time.sleep(5)
        self.select_qty(qty)
        self.delete_item()
        self.switch_to_default_windows()

    def validate_checkout_process(self):
        self.click_on_product()
        self.windows_handle()
        time.sleep(10)
        self.click_buy_now()
        time.sleep(20)
        self.get_address()
        self.payment_method()
        self.order_review()

    def select_each_payment_method(self):
        self.click_payment_radio_btn()
        time.sleep(5)

    def check_user_apply_coupon_code(self):
        self.click_use_payment_btn()
        time.sleep(10)
        self.enter_coupon_code()
        self.click_apply_btn()
        time.sleep(10)

    def give_ratings(self, URL):
        self.switch_to_default_windows()
        time.sleep(10)
        self.driver.get(URL)
        self.click_on_orders()
        time.sleep(30)
        self.select_order_year()
        self.click_Write_product_review()
        self.click_ratings()
        time.sleep(5)




