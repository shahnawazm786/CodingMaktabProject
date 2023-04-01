
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
select_element = driver.find_element(By.NAME, 'my-select')
select = Select(select_element)
select.select_by_value("1")
select.select_by_visible_text("Two")
time.sleep(5)
driver.quit()
