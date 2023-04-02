from selenium import webdriver
import time

from selenium.webdriver.common.by import By
driver=webdriver.Chrome()
driver.implicitly_wait(5)
driver.get('https://www.jqueryscript.net/tags.php?/event%20calendar/')
frame=driver.find_element(By.ID,value="aswift_1")
driver.switch_to.frame(frame)
time.sleep(5)
driver.quit()