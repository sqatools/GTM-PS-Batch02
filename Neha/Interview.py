from selenium import webdriver
from selenium.webdriver.common.by import By


# Open Caratlane.in
driver = webdriver.Chrome()
driver.get("https://www.amazon.in/")
driver.maximize_window()
