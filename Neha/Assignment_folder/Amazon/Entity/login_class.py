from Base.functions import AmazonBase
from .Login_locator import *


class login(AmazonBase):

    def __init__(self, driver):
        super().__init__(driver)

    def click_nevigation(self,Signin_mousehover_locator):
        self.mousehover_move_to_element(Signin_mousehover_locator)

    def Signin_click(self,Signin_locator):
        self.click_element(Signin_locator)

    def enter_mobile_no(self,Mobileno_locator):
        self.enter_values(Mobileno_locator, Mobileno_data)

    def continue_button(self, continue_button_locator):
        self.click_element(continue_button_locator)

    def passwrd(self, Password_locator):
        self.enter_values(Password_locator,Password_data)

    def login_button(self, login_btn):
        self.click_element(login_button)

    def provide_login_details(self,
                                Mobileno_data: str,
                                Password_data: str):
        self.click_nevigation()
        self.Signin_click()
        self.enter_mobile_no(Mobileno_data)
        self.continue_button()
        self.passwrd(Password_data)
        self.login_button()