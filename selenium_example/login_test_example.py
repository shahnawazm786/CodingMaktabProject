from selenium import webdriver
import time
from selenium.webdriver.common.by import By
driver=webdriver.Chrome()
driver.implicitly_wait(5)
driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
title=driver.title
print(title)
userText=driver.find_element(by=By.NAME,value="username")
userText.clear()
userText.send_keys("admin")
passWordText=driver.find_element(by=By.NAME,value="password")
passWordText.clear()
passWordText.send_keys("admin123")
loginButton=driver.find_element(by=By.TAG_NAME,value="button")
loginButton.click()
time.sleep(10)
driver.quit()