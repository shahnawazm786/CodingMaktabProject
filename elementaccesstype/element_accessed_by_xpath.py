from selenium import webdriver
import time

from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
driver=webdriver.Chrome()
driver.implicitly_wait(5)
driver.get('https://www.selenium.dev/selenium/web/web-form.html')
time.sleep(5)
header=driver.find_element(By.XPATH,value='html/body/main/div/div/div/h1')
print(header.text)

head=driver.find_element(By.XPATH,value='//h1')
print('This output form refencial xpath ->  '+head.text)
driver.quit()
