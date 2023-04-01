from selenium import webdriver
import time

from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
driver=webdriver.Chrome()
driver.implicitly_wait(5)
driver.get('https://www.selenium.dev/selenium/web/web-form.html')
time.sleep(5)
'''
try:
    inputText=driver.find_element(By.CLASS_NAME,value="form-label w-100")
    inputText.send_keys("By class accessed")
except(NoSuchElementException):
    inputText = driver.find_element(By.CLASS_NAME, value="form-label")
    inputText.send_keys("By class accessed")
'''

time.sleep(15)
driver.quit()