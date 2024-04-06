import time

from SQA_Locator import *
from functions_file import *
from Testdata_file import *




get_driver(web_URL ,'Chrome',timeout=350)
send_data(Firstname, Firstname_locator)
send_data(LastName, LastName_locator)
time.sleep(5)
send_data(DOB, DOB_locator)
click_element(male_rdbtn_locator)
click_element(female_rdbtn_locator)
