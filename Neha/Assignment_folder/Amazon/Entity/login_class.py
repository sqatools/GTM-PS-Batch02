from Base.functions import functions
from .Login_locator import *


class login(AmazonBase):

    def __init__(self, driver):
        super().__init__(driver)

    def click_nevigation(self,Signin_mousehover):
        self.mousehover_move_to_element(Signin_mousehover_locator)

    def Signin_click(self,Signin_btn):
        self.click_element(Signin_locator)

    def enter_mobile_no(self,Mobileno):
        self.enter_values(Mobileno_locator)

    def continue_button(self, continue_btn):
        self.click_element(continue_button_locator)

    def passwrd(self, Password):
        self.enter_values(Password_locator)

    def login_button(self, login_btn):
        self.click_element(login_button)

    def provide_login_details(self,
                                Mobileno: str,
                                continue_btn: str,
                                passwrd: str):
        self.click_nevigation()
        self.Signin_click()
        self.enter_mobile_no(Mobileno)
        self.continue_button(continue_btn)
        self.passwrd(passwrd)
        self.login_button()