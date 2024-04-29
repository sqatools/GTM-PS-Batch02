from base.base_functions import SeleniumBase
from .Amazon_locater import *
from utilities.get_logger import logger
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
        self.click_element("//div[@id='departments']//span[text()="+category+"]")

    def choose_brand(self, brand):
        self.click_element("//span[text()="+brand+"]//..//..//input[@type='checkbox'")

    def choose_price_range(self, price_range):
        self.click_element("//a//span[text()="+price_range+"]")

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




#------------------------------------------------------------------------------
    def register_new_user(self, new_username, new_mobile, new_pw):
        self.navigate_to_signin()
        self.create_new_account()
        self.enter_new_name(new_username)
        self.enter_new_phone(new_mobile)
        self.enter_new_password(new_pw)
        self.click_verify_mobile_no()

    def enter_login_data(self, email, password):
        self.enter_email(email)
        self.click_continue()
        self.enter_password(password)
        self.click_signin()

    def enter_incorrect_login_data(self, incorrect_email):
        self.enter_email(incorrect_email)
        self.click_continue()
        self.varify_incorrect_email_error_msg()

    def search_for_product(self,product_name):
        self.enter_product_name_and_search(product_name)
        self.varify_search_result(product_name)

    def search_product_with_filters(self, category, brand, price_range):
        self.choose_category(category)
        self.choose_brand(brand)
        self.choose_price_range(price_range)

    def check_all_product_details(self):
        self.get_name()
        self.get_price()
        self.get_description()
        self.get_review()

    def shopping_cart_add_item(self):
        self.click_add_to_cart()
        self.verify_item_added_to_cart()



