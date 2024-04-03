import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://automationbysqatools.blogspot.com/p/code-practice.html")
driver.maximize_window()
driver.implicitly_wait(10)
driver.find_element(By.NAME, "q").send_keys("Python Selenium")
driver.find_element(By.XPATH, "//td[@class='gsc-search-button']//following::input[@type='submit']").click()
driver.find_element(By.NAME, "q").clear()



# driver.find_element(By.XPATH, "//li[@class='selected']//following-sibling::a[text()='Home']").click()
driver.find_element(By.XPATH, "//div[@class='widget-content']//following-sibling::a[text()='Home']").click()
driver.find_element(By.XPATH, "//div[@class='widget-content']//following-sibling::a[text()='Code Practice']").click()
driver.find_element(By.XPATH, "//div[@class='widget-content']//following-sibling::a[text()='Pytest Framework']").click()
driver.find_element(By.XPATH, "//div[@class='widget-content']//following-sibling::a[text()='Python 3 Tutorial']").click()
driver.find_element(By.XPATH, "//div[@class='widget-content']//following-sibling::a[text()='Python Selenium']").click()
driver.find_element(By.XPATH, "//div[@class='widget-content']//following-sibling::a[text()='Manual Testing']").click()
driver.find_element(By.XPATH, "//div[@class='widget-content']//following-sibling::a[text()='API Testing']").click()
driver.find_element(By.XPATH, "//div[@class='widget-content']//following-sibling::a[text()='API Testing']").click()
driver.find_element(By.XPATH, "//div[@class='widget-content']//following-sibling::a[text()='Github']").click()
driver.find_element(By.XPATH, "//div[@class='widget-content']//following-sibling::a[text()='Online Training']").click()
driver.find_element(By.XPATH, "//div[@class='widget-content']//following-sibling::a[text()='Robot Framework']").click()
driver.find_element(By.XPATH, "//div[@class='widget-content']//following-sibling::a[text()='Home']").click()

# (//td[@align='center'])[1]

time.sleep(20)
driver.close()