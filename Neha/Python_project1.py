from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Open Amazon.in
driver = webdriver.Chrome()
driver.get("https://www.amazon.in/")
driver.maximize_window()
search_item = "mobile"  # Replace with your desired search item
search_box = driver.find_element(By.ID,"twotabsearchtextbox")
search_box.send_keys(search_item)
search_box.send_keys(Keys.RETURN)


# scenario 1: Verify that the cart icon shows the item count (numeric value)
first_result = driver.find_element(By.CSS_SELECTOR,".s-result-item")
wait = WebDriverWait(driver, 10)
add_to_cart_button = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, ".a-button-input")))
add_to_cart_button.click()
try:
    cart_count_element = driver.find_element(By.ID, "nav-cart-count")
    cart_count = int(cart_count_element.text.strip())
    print(f"Cart count: {cart_count} item(s)")
except NoSuchElementException:
    print("Cart icon not found or does not display the item count.")

# scenario 2: Verify that location is not null or blank
location = driver.find_element(By.ID,"glow-ingress-line1")
if location.text.strip():
    print(f"Location: {location.text.strip()}")
else:
    print("Location is null or blank.")

# Scenario 3: Verify that items list is displayed based on search item
items_list = driver.find_elements(By.CSS_SELECTOR,".s-result-item")
if items_list:
    print(f"Found {len(items_list)} items for '{search_item}'")
else:
    print(f"No items found for '{search_item}'")

# Close the browser
driver.quit()