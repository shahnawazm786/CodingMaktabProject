#my-disabled

from selenium import webdriver
import time

from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
driver=webdriver.Chrome()
driver.implicitly_wait(5)
driver.get('https://www.selenium.dev/selenium/web/web-form.html')
time.sleep(5)
ele=driver.find_element(By.NAME,value='my-disabled')
if ele.is_displayed()==True:
    print('Displayed')
else:
    print('Not Displayed')

if ele.is_enabled()==True:
    print('Enable to enter the value')
else:
    print('it is disabled')

radio=driver.find_element(By.ID,value="my-radio-1")
if radio.is_selected()==True:
    print('Radio button is selected')
else:
    print('Radio button is not selected')

