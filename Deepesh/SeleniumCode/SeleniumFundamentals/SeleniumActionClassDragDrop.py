import time

from selenium import  webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.action_chains import ActionChains
driver = webdriver.Chrome()
driver.get("https://www.globalsqa.com/demo-site/draganddrop/")
driver.maximize_window()
wait = WebDriverWait(driver, 20)

def move_to_element(element):
    action = ActionChains(driver)
    action.move_to_element(element)
    action.perform()

def click_to_element(element):
    action = ActionChains(driver)
    action.click(element)
    action.perform()

def drag_and_drop(elem1, elem2):
    action = ActionChains(driver)
    action.drag_and_drop(elem1, elem2)
    action.perform()

def context_click(elem1):
    action = ActionChains(driver)
    action.context_click(elem1)
    action.perform()

iframe_element = wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, "iframe[class='demo-frame lazyloaded']")))
driver.switch_to.frame(iframe_element)

# image1 = wait.until(ec.visibility_of_element_located((By.XPATH, "//ul[@id='gallery']/li[1]")))
trash = wait.until(ec.visibility_of_element_located((By.XPATH, "//div[@id='trash']")))
# drag_and_drop(image1, trash)
# image2 = wait.until(ec.visibility_of_element_located((By.XPATH, "//ul[@id='gallery']/li[1]")))
# drag_and_drop(image2, trash)
# image3 = wait.until(ec.visibility_of_element_located((By.XPATH, "//ul[@id='gallery']/li[1]")))
# drag_and_drop(image3, trash)
# time.sleep(10)

context_click(trash)

time.sleep(10)

driver.close()
