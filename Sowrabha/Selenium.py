import time
#
from selenium import webdriver
from selenium.webdriver.common.by import By
#
# driver = webdriver.Chrome()
# driver.get("https://www.google.co.in")
# driver.maximize_window()
# driver.implicitly_wait(10)
# driver.find_element(By.NAME, "q").send_keys("Python Selenium")
# driver.find_element(By.NAME, "btnK").click()
# time.sleep(5)
# driver.close()


###################basic xpath#############
# driver = webdriver.Chrome()
# driver.maximize_window()
# driver.implicitly_wait(10)
# driver.get("https://automationbysqatools.blogspot.com/p/code-practice.html")
# driver.find_element(By.XPATH, "//a[@href='/2020/07/python-basic-program.html']").click()
# time.sleep(5)
# driver.close()

###############Text Method #################################
# driver = webdriver.Chrome()
# driver.maximize_window()
# driver.implicitly_wait(10)
# driver.get("https://automationbysqatools.blogspot.com/p/code-practice.html")
# driver.find_element(By.XPATH, "//a[text()='Pytest Framework']").click()
# time.sleep(5)
# driver.close()

###############contains method######################
driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(10)
driver.get("https://automationbysqatools.blogspot.com/p/code-practice.html")
driver.find_element(By.XPATH, "//a[contains(@href,'api-testing-fundamentals')]").click()
time.sleep(5)
driver.close()


#################Indexing in the xpath##########################

