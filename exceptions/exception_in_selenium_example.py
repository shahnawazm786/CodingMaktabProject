from selenium import webdriver
import time

from selenium.common import NoSuchElementException, StaleElementReferenceException
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By


driver=webdriver.Chrome()
driver.implicitly_wait(5)
driver.get('https://www.google.com')
ele=driver.find_element(By.NAME,value="q")
ele.send_keys("kaz-it training hub"+Keys.ENTER)
time.sleep(5)
#ele=driver.find_element(By.NAME,value="q")
try:
    ele.send_keys("Automation"+Keys.ENTER)
except(StaleElementReferenceException):
    ele = driver.find_element(By.NAME, value="q")
ele.clear()
ele.send_keys("Automation"+Keys.ENTER)
time.sleep(5)

