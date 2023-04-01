from selenium import webdriver
import time

from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
driver=webdriver.Chrome()
driver.implicitly_wait(5)
driver.get('https://www.selenium.dev/selenium/web/web-form.html')
time.sleep(5)
passw=driver.find_element(By.XPATH,value="//input[@type='password']")
passw.send_keys('123456789')
time.sleep(5)
driver.quit()