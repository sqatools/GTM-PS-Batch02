from selenium.webdriver.common.by import By
from data.amazon_data import *

# search locator
search_bar_locator = (By.ID, "twotabsearchtextbox")
search_icon_locator = (By.ID, "nav-search-submit-button")
filter_by_category_locator = (By.XPATH,"""//span[contains(text(), "Women's Running Shoes")]//parent::a""")
filter_by_price_locator = (By.XPATH, "//span[contains(text(),'"+amazon_test_data["search"]["price_range"]+"')]")
filter_by_brand_locator = (By.XPATH, "//span[@class='a-list-item']//span[contains(text(),'"+ amazon_test_data["search"]["brand"] +"')]")

# product details

product_details_locator =  (By.XPATH, "(//span[@data-component-type='s-product-image']//img[@class='s-image'])[3]")
name_text_locator = (By.XPATH, "//span[@id='productTitle']")
price_text_locator = (By.XPATH, "//div[@id='apex_desktop']//span[@class='a-price-whole']")
description_text_locator = (By.XPATH, "//div[@id='productDescription']//span")
reviews_text_locator = (By.XPATH, "//span[@data-hook='rating-out-of-text']")

# add to cart
add_to_cart_btn_locator = (By.ID, "add-to-cart-button")
item_added_to_cart_txt_locator = (By.XPATH, "//div[@class='a-fixed-left-grid-inner']//h1[contains(text(),'Added to Cart')]")
go_to_cart_locator = (By.ID, "nav-cart")
select_qanty_dropdown_locator = (By.XPATH, "//select[@id='quantity']")
delete_item_locator = (By.XPATH, "//input[@value='Delete']")
buy_now_locator = (By.XPATH, "//input[@id='buy-now-button']")

