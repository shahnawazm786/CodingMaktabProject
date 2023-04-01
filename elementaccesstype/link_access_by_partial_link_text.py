from selenium import webdriver
import time
from selenium.webdriver.common.by import By
driver=webdriver.Chrome()
driver.implicitly_wait(5)
driver.get('https://www.selenium.dev/selenium/web/web-form.html')
time.sleep(5)
link=driver.find_element(By.PARTIAL_LINK_TEXT,value="Return")
link.click()
time.sleep(5)
driver.quit()