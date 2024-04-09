from selenium.webdriver.chrome import webdriver

from behave import *


@given ('Launch the browser')
def launch_browser(context):
    context.driver = webdriver.Chrome()

@when('Open the Application')
@When ('Enter the username')
def Enter_username(context):
    cont