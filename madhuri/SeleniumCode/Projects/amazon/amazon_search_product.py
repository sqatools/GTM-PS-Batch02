import time
from amazon_locator import *
from amazon_functions import *
from amazon_data import *

driver, wait = get_driver()

send_data(search_bar_locator,'shoes')
click_element(search_icon_locator)
time.sleep(2)
click_element(filter_by_price_locator)
time.sleep(10)
# //span[@class='a-price-whole']