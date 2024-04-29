import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

# Set up WebDriver (you need to download the appropriate driver for your browser)
driver = webdriver.Chrome()  # Change to webdriver.Firefox() if using Firefox
driver.maximize_window()

# Navigate to Amazon
driver.get("https://www.amazon.com/")

# Locate sign-in link and click it

sign_in_link = driver.find_element(By.ID, "nav-link-accountList")
sign_in_link.click()

# Fill in login details and sign in

email_input = driver.find_element(By.ID, "ap_email")
email_input.send_keys("madhuri.rahane66@gmail.com")
password_input = driver.find_element(By.ID, "ap_password")
password_input.send_keys("29nikhil_m")
password_input.send_keys(Keys.RETURN)

# Wait for login process to complete
time.sleep(3)  # You may need to adjust the waiting time

# Navigate to profile page

profile_link = driver.find_element(By.XPATH, "//a[@href='/gp/profile']")
profile_link.click()

# Edit profile information (example: changing the name)
edit_button = driver.find_element(By.XPATH, "//a[@id='huc_edit']")
edit_button.click()

# Locate the name input field and change the value
name_input = driver.find_element(By.ID, "ap_customer_name")
name_input.clear()
name_input.send_keys("madhuri gaikar")

# Save changes
save_button = driver.find_element(By.XPATH, "//input[@type='submit']")
save_button.click()

# Close the browser
driver.quit()

"""
no_orders_text = "0 orders"
no_orders_text_list = no_orders_text.split(" ")
print(no_orders_text_list[0])
count = no_orders_text_list[0]
if int(count) == 0:
    print("zero")
else:
    print("more than 0")
"""

"""
    # func
    # module
    class
    package
    session
    priproty whioe pytest excecution
    
    marker: grouping of test cases
    fixture:  function, module scope, class scope, package scope, session scope
    
    test_ is complusry otherwise it wont be execute that function
    test function only we can use paramterized values
"""

