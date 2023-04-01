from selenium import webdriver
import time


from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By


driver=webdriver.Chrome()
driver.implicitly_wait(5)
driver.get('https://www.selenium.dev/selenium/web/web-form.html')
time.sleep(5)
element=driver.find_element(By.XPATH,value="//input[@name='my-range']")
action=ActionChains(driver)
action.drag_and_drop_by_offset(element,20,100).perform()
time.sleep(5)
driver.quit()