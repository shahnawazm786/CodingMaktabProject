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
element=driver.find_element(By.XPATH,value="//input[@name='my-date']")
element.click()
time.sleep(5)
#day=driver.find_elements(By.XPATH,value="//td[@class='day']")
day=driver.find_elements(By.XPATH,value="//table//tbody//tr//td")

for d in day:

    if d.text=='14':
        print("14 found")
        print(d.tag_name)
        d.click()
        break

   # print(d.text, end="\t")

time.sleep(10)
driver.close()