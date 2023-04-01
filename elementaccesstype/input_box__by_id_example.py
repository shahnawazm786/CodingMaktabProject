from selenium import webdriver
import time
from selenium.webdriver.common.by import By
driver=webdriver.Chrome()
driver.implicitly_wait(5)
driver.get('https://www.selenium.dev/selenium/web/web-form.html')
time.sleep(5)
inputelement=driver.find_element(By.ID,value="my-text-id")
inputelement.send_keys("pragayan@gmail.com")
time.sleep(5)
driver.quit()
