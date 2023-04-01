from selenium import webdriver
import time

from selenium.webdriver.common.by import By

driver=webdriver.Chrome()
driver.implicitly_wait(5)
driver.get('https://www.selenium.dev/selenium/web/web-form.html')
time.sleep(5)
radio=driver.find_elements(By.XPATH,value="//input[@name='my-radio']")
for r in radio:
    if(r.is_selected()):
        r.click()
    else:
        r.click()

# take the screenshot
driver.save_screenshot("./fullpage.png")
driver.save_screenshot("./screenshot/fullpage.png")
driver.close()