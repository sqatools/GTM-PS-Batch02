from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import *

# Initialize the WebDriver (you can choose Chrome, Firefox, etc.)
driver = webdriver.Chrome()  # Set the correct path

# Open Amazon.in
driver.get("https://www.amazon.in/")
driver.maximize_window()

# Scenario a: Verify that the add to cart icon shows only numbers
search_item = "laptop"  # Replace with your desired search item
search_box = driver.find_element(By.ID ,"twotabsearchtextbox")

search_box.send_keys(search_item)
search_box.send_keys(Keys.RETURN)

# Assuming the first search result is the item we want to test
first_result = driver.find_element(By.CSS_SELECTOR,".s-result-item")
wait = WebDriverWait(driver, 10)  # Wait up to 10 seconds

try:
    # add_to_cart_icon = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, ".a-price-symbol")))
    add_to_cart_icon = wait.until(EC.presence_of_element_located((By.ID, "nav-cart-count")))
    if add_to_cart_icon.text.strip().isdigit():
        print(f"Add to cart icon shows the item number: {add_to_cart_icon.text.strip()}")
    else:
        print("Add to cart icon does not display the item number")
except NoSuchElementException:
    print("Add to cart icon not found.")



# first_result = driver.find_element(By.CSS_SELECTOR,".s-result-item")
# wait = WebDriverWait(driver, 10)  # Wait up to 10 seconds
# add_to_cart_icon = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, ".a-price-symbol")))
# #add_to_cart_icon = first_result.find_element(By.CSS_SELECTOR,".a-price-symbol")
# if add_to_cart_icon.text.strip() == "₹":
#     print("Add to cart icon shows the price symbol (not a number)")
# else:
#     print("Add to cart icon shows a number")

# Scenario b: Verify that location is not null or blank
location = driver.find_element(By.ID,"glow-ingress-line2")
if location.text.strip():
    print(f"Location: {location.text.strip()}")
else:
    print("Location is null or blank")

# Scenario c: Verify that items list is displayed based on search item
items_list = driver.find_elements(By.CSS_SELECTOR,".s-result-item")
if items_list:
    print(f"Found {len(items_list)} items for '{search_item}'")
else:
    print(f"No items found for '{search_item}'")

# Close the browser
driver.quit()