from selenium.webdriver.common.by import By

search_bar_locator = (By.ID, "twotabsearchtextbox")
search_icon_locator = (By.ID, "nav-search-submit-button")
filter_by_price_locator = (By.XPATH, "//span[contains(text(),'Under ₹500')]")
product_details_locator = (By.TAG_NAME,"//img[@alt='Sponsored Ad - Campus Mens Terminator (N) Running Shoes']" )



