from selenium import webdriver
import time


from selenium.common import NoSuchElementException, ElementNotInteractableException
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
driver=webdriver.Chrome()
driver.implicitly_wait(5)
driver.get('https://www.selenium.dev/selenium/web/web-form.html')
time.sleep(5)
readonly=driver.find_element(By.XPATH,value="//input[@name='my-readonly']")