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
radio=driver.find_elements(By.XPATH,value="//input[@name='my-radio']")
for r in radio:
    if(r.is_selected()):
        r.click()
    else:
        r.click()
time.sleep(5)
driver.close()
