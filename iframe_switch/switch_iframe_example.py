from selenium import webdriver
import time

from selenium.webdriver.common.by import By
driver=webdriver.Chrome()
driver.implicitly_wait(5)
driver.get('https://www.jqueryscript.net/tags.php?/event%20calendar/')
frame=driver.find_element(By.ID,value="aswift_1")
driver.switch_to.frame(frame) #id
driver.switch_to.parent_frame() #parent
driver.switch_to.frame(1) #frame1
driver.switch_to.default_content()# parent
time.sleep(5)
driver.quit()