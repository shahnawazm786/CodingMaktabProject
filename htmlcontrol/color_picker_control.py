from selenium import webdriver
import time


from selenium.common import NoSuchElementException, ElementNotInteractableException
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.color import Color
from selenium.webdriver.support.select import Select

driver=webdriver.Chrome()
driver.implicitly_wait(5)
driver.get('https://www.selenium.dev/selenium/web/web-form.html')
time.sleep(5)
colors=driver.find_element(By.XPATH,value="//input[@name='my-colors']")
colors.click()
for i in range(100):
    colors.send_keys(Keys.ARROW_RIGHT)
    colors.click()
#colors.send_keys(Keys.ARROW_RIGHT)
#colors.send_keys(Keys.ARROW_RIGHT)
colors.click()
time.sleep(15)
driver.close()