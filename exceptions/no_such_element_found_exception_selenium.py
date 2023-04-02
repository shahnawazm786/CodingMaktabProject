from selenium import webdriver
import time

from selenium.common import NoSuchElementException, StaleElementReferenceException
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By


driver=webdriver.Chrome()
driver.implicitly_wait(5)
driver.get('https://www.google.com')
try:
    ele=driver.find_element(By.NAME,value="q1")
except(NoSuchElementException):
    ele = driver.find_element(By.NAME, value="q")
ele.send_keys("kaz-it training hub"+Keys.ENTER)
driver.quit()