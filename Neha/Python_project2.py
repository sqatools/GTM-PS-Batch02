# Required libraries
import time
import os
import csv
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Initialize WebDriver (using Chrome in this example)
driver = webdriver.Chrome() # Set the correct path to chromedriver

# Step 1: Launch the browser
driver.get("http://www.google.com")

# Step 2: Enter the keyword "amazon" in the search bar
search_bar = driver.find_element(By.NAME, "q")
search_bar.send_keys("amazon")
search_bar.send_keys(Keys.RETURN)

# Step 3: Print all the search results
search_results = driver.find_elements(By.XPATH, "//h3")
for result in search_results:
    print(result.text)

# Step 4: Click on the link which takes you to the Amazon login page
amazon_link = driver.find_element(By.PARTIAL_LINK_TEXT, "Amazon")
amazon_link.click()

# Step 5: Login to https://www.amazon.in/
# (You'll need to manually log in or automate the login process)

# Step 6: Click on all buttons on search & select Electronics
# (You'll need to identify the buttons and implement the clicks)

# Step 7: Search for Dell computers
search_bar_amazon = driver.find_element(By.ID, "twotabsearchtextbox")
search_bar_amazon.clear()
search_bar_amazon.send_keys("dell computers")
search_bar_amazon.send_keys(Keys.RETURN)

# Step 8: Apply the filter of range Rs 30000 to 50000
# (You'll need to identify the filter elements and apply the range)

# Step 9: Validate all the products on the first 2 pages are shown in the range of Rs 30000 to 50000
# (You'll need to verify the product prices)

# Step 10: Print all the products on the first 2 pages whose rating is 5 out of 5
# (You'll need to identify the rating elements and extract relevant information)

# Step 11: Add the first product whose rating is 5 out of 5 to the wish list (Create a new wish list)
# (You'll need to identify the add-to-wishlist button and perform the action)

# Step 12: Validate the product is added to the wish list
# (You'll need to verify the wish list contents)

# Close the browser
driver.quit()