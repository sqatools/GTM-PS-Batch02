from base.selenium_base import SeleniumBase


class DummyWebsite(SeleniumBase):
    def __init__(self, driver):
        super().__init__(driver)


    def enter_first_name(self, first_name):
        self.enter_value()
