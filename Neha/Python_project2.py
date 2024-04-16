# Required libraries
import time
import os
import csv
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.action_chains import ActionChains

# Initialize WebDriver (using Chrome in this example)
driver = webdriver.Chrome()
driver.get("http://www.google.com")
driver.maximize_window()

# Step 2: Enter the keyword "amazon" in the search bar
search_bar = driver.find_element(By.NAME, "q")
search_bar.send_keys("amazon")
search_bar.send_keys(Keys.RETURN)
time.sleep(5)

# Step 3: Print all the search results
search_results = driver.find_elements(By.XPATH, "//h3")
for result in search_results:
    print(result.text)

# Step 4: Click on the link which takes you to the Amazon login page
amazon_link = driver.find_element(By.PARTIAL_LINK_TEXT, "Amazon")
amazon_link.click()

# Step 5: Login to https://www.amazon.in/
try:
    sign_in_button = driver.find_element(By.ID, "nav-link-accountList")
    sign_in_button.click()
    driver.implicitly_wait(3)
    phone_number_input = driver.find_element(By.ID, "ap_email")  # Replace with the actual ID of the phone input field
    phone_number_input.send_keys("+917503308660")  # Replace with the desired phone number
    driver.implicitly_wait(3)
    continue_button = driver.find_element(By.XPATH, "//input[@id = 'continue']")
    continue_button.click()
    password_input = driver.find_element(By.ID,"ap_password")
    password_input.send_keys("Qwerty123#")
    Signin_button = driver.find_element(By.ID, "signInSubmit")
    Signin_button.click()
    time.sleep(5)
except Exception as e:
    print(f"An error occurred: {str(e)}")


#Step 6: Click on all buttons on search & select Electronics
all_button = driver.find_element(By.ID,"nav-search-dropdown-card")
all_button.click()
driver.implicitly_wait(5)
try:
    dropdown = Select(driver.find_element(By.ID,"searchDropdownBox"))
    driver.implicitly_wait(3)
    dropdown.select_by_visible_text("Electronics")
except Exception as e:
    print(f"An error occurred: {str(e)}")

# # Step 7: Search for Dell computers
try:
    wait = WebDriverWait(driver, 10)
    search_bar_amazon = wait.until(EC.visibility_of_element_located((By.ID, "twotabsearchtextbox")))
    search_bar_amazon.clear()
    search_bar_amazon.send_keys("dell computers")
    search_bar_amazon.send_keys(Keys.RETURN)
    driver.implicitly_wait(5)
    # # Step 8: Apply the filter of range Rs 30000 to 50000
    min_price_input = wait.until(EC.presence_of_element_located((By.ID, "low-price")))
    max_price_input = wait.until(EC.presence_of_element_located((By.ID, "high-price")))
    min_price_input.clear()
    min_price_input.send_keys("30000")
    max_price_input.clear()
    max_price_input.send_keys("50000")
    max_price_input.send_keys(Keys.RETURN) #done
except TimeoutException:
    print("Timed out waiting for elements.")
# # Step 11: Add the first product whose rating is 5 out of 5 to the wish list (Create a new wish list)
# # Step 12: Validate the product is added to the wish list
# wait = WebDriverWait(driver, 20)
# wait.until(EC.presence_of_element_located((By.CLASS_NAME, "s-main-slot s-result-list s-search-results sg-row")))

# Find the first product with a 5-star rating
product_link = driver.find_element(By.XPATH, "//span[contains(text(),'5.0 out of 5 stars')]")
ActionChains(driver).move_to_element(product_link).perform()

# Click on the "Add to Wish List" button
driver.implicitly_wait(3)
add_to_wishlist_button = driver.find_element(By.ID, "a-autoid-31-announce")
add_to_wishlist_button.click()
driver.implicitly_wait(3)

# Create a new wishlist (if not already created)
try:
    create_new_wishlist_button = driver.find_element(By.ID, "WLNEW_create")
    create_new_wishlist_button.click()
except:
    pass

# Validate that the product is added to the wishlist
driver.implicitly_wait(3)
wishlist_link = driver.find_element(By.ID, "nav-link-wishlist")
wishlist_link.click()

# Check if the product is listed in the wishlist
driver.implicitly_wait(3)
product_in_wishlist = driver.find_element(By.CSS_SELECTOR, ".g-items-section .g-item-sortable")
assert "laptop" in product_in_wishlist.text, "Product not added to wishlist"
print("Product successfully added to wishlist!")




# # # Step 9: Validate all the products on the first 2 pages are shown in the range of Rs 30000 to 50000
#     # Extract product details from the first 2 pages
#     for page in range(2):
#         wait = WebDriverWait(driver, 10)
#         product_elements = wait.until(EC.visibility_of_element_located((By.XPATH, "//span[@type='s-search-results']")))
#
#         # Extract and validate prices
#         for product in product_elements:
#             try:
#                 product_name = product.find_element(By.XPATH, "//h1[@class = 'a-size-base s-desktop-toolbar a-text-normal']//following::span[@class= 'a-size-medium a-color-base a-text-normal']").text
#                 # Extract product price
#                 price_element = product.find_element(By.CSS_SELECTOR, ".a-price .a-offscreen']")
#                 driver.implicitly_wait(3)
#                 price = float(price_element.text.replace("₹","").replace(",",""))
#                 driver.implicitly_wait(3)
#                 if 30000 <= price <= 50000:
#                     print(f"Product: {product_name} | Price: ₹{price:.2f}")
#                 else:
#                     print(f"Product: {product_name} | Invalid Price: ₹{price:.2f}")
#             except Exception as e:
#                 print(f"Error: {str(e)}")
#
#         # Go to the next page
#         if page == 0:
#          next_page_button = driver.find_element(By.XPATH,"//a[@class = 's-pagination-item s-pagination-next s-pagination-button s-pagination-separator']")
#          next_page_button.click()
#
#     """
#     for page in range(2):
#         # Locate product elements
#         product_elements = driver.find_elements(By.CSS_SELECTOR, ".s-result-item")
#
#         # Extract and validate ratings
#         for product in product_elements:
#             try:
#                 # Extract product name
#                 product_name = product.find_element(By.CSS_SELECTOR, ".a-text-normal").text
#
#                 # Extract product rating
#                 rating_element = product.find_element(By.CSS_SELECTOR, ".a-icon-star-small")
#                 rating = float(rating_element.get_attribute("innerHTML").split()[0])
#
#                 if rating == 5.0:
#                     print(f"Product: {product_name} | Rating: {rating:.1f}")
#             except Exception as e:
#                 print(f"Error: {str(e)}")
#
#         # Go to the next page
#         if page == 0:
#             next_page_button = driver.find_element(By.CSS_SELECTOR, ".s-pagination-next")
#             next_page_button.click()
#
#     # Add the first 5-star rated product to the wish list (you can implement this part)
#
# except TimeoutException:
#     print("Timed out waiting for elements.")
#     """
#
# except Exception as e:
#      print(f"An error occurred: {str(e)}")
#
#
# # # Step 10: Print all the products on the first 2 pages whose rating is 5 out of 5
# # # (You'll need to identify the rating elements and extract relevant information)
# # product_elements = driver.find_elements(By.CSS_SELECTOR, ".s-result-item")
# #
# # # Print product names with a 5-star rating
# # for product in product_elements:
# #     try:
# #         product_name = product.find_element(By.CSS_SELECTOR, ".a-text-normal").text
# #         rating_element = product.find_element(By.CSS_SELECTOR, ".a-icon-star-small")
# #         rating = float(rating_element.get_attribute("innerHTML").split()[0])
# #         if rating == 5.0:
# #             print(f"Product: {product_name} | Rating: {rating:.1f}")
# #     except Exception as e:
# #         print(f"Error: {str(e)}")
#
# """"""




