from selenium import webdriver
import time


from selenium.webdriver.common.by import By


from utils.selenium_utils_method import selenium_common_function

driver=webdriver.Chrome()
driver.implicitly_wait(5)
driver.get('https://www.selenium.dev/selenium/web/web-form.html')

element=driver.find_element()
e=selenium_common_function.waitTillElementClickable(driver,element,20)
element.click()
selenium_common_function.waitTillLoading(element,20)
