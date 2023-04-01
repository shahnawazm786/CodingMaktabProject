from selenium import webdriver
import time


from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
driver=webdriver.Chrome()
driver.implicitly_wait(5)
driver.get('https://www.selenium.dev/selenium/web/web-form.html')
time.sleep(5)
passw=driver.find_element(By.XPATH,value="//textarea[@name='my-textarea']")
passw.send_keys('Hello',Keys.ENTER)
passw.send_keys('Hello1',Keys.ENTER)
passw.send_keys('Hello2',Keys.ENTER)
time.sleep(5)
driver.quit()