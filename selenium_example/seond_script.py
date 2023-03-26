from selenium import webdriver
import time

driver=webdriver.Chrome()
driver.implicitly_wait(5)
driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
title=driver.title
print(title)
lenght_of_title=len(title)
assert lenght_of_title > 0
assert title == 'web form'
time.sleep(10)

#find_element()
#find_elements()