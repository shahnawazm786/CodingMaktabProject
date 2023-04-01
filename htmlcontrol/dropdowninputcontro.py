
from selenium import webdriver
import time


from selenium.common import NoSuchElementException, ElementNotInteractableException
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select

driver=webdriver.Chrome()
driver.implicitly_wait(5)
driver.get('https://www.selenium.dev/selenium/web/web-form.html')
time.sleep(5)
drp=driver.find_element(By.XPATH,value="//input[@name='my-datalist']")
drp.send_keys("San Fransico")
time.sleep(5)
drp.clear()
drp.click()
time.sleep(5)
drp.send_keys('New York')
drp.send_keys(Keys.ESCAPE)
time.sleep(5)
driver.quit()
