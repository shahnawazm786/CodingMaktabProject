from selenium import webdriver
import time


from selenium.common import NoSuchElementException, ElementNotInteractableException
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
driver=webdriver.Chrome()
driver.implicitly_wait(5)
driver.get('https://www.selenium.dev/selenium/web/web-form.html')
time.sleep(5)
passw=driver.find_element(By.XPATH,value="//input[@name='my-disabled']")
try:
    passw.send_keys('Hello')
except(ElementNotInteractableException):
    print('we can not add text in the disabled input box')
    print(passw.text)
time.sleep(5)
driver.quit()