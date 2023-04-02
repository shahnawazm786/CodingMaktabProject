from selenium import webdriver
import time

from selenium.common import NoSuchElementException, ElementNotInteractableException
from selenium.webdriver.common.by import By
driver=webdriver.Chrome()
driver.implicitly_wait(5)
driver.get('https://www.selenium.dev/selenium/web/web-form.html')
time.sleep(5)
ele=driver.find_element(By.NAME,value="my-disabled")
try:
    ele.send_keys("Hello")
except(ElementNotInteractableException):
    print('Element is disabled')
    print('You cannot pass the value')
    ele.screenshot("./disable.png")
    driver.save_screenshot("./disabled_element_page.png")
time.sleep(5)
driver.close()
