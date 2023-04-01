from selenium import webdriver
import time

from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
driver=webdriver.Chrome()
driver.implicitly_wait(5)
driver.get('https://www.selenium.dev/selenium/web/web-form.html')
time.sleep(5)
try:
    '''
    1. Locator is not present in the page
    2. May be used wrong accessbility
    3. Loctor is there you use right accessibility but element is taking time to load 
    '''
    link=driver.find_element(By.LINK_TEXT,value="Return")

except(NoSuchElementException):
    print("I am using link text here")
    link = driver.find_element(By.LINK_TEXT, value="Return to index")
finally:
    print('we achieved it')
link.click()
time.sleep(5)
driver.quit()