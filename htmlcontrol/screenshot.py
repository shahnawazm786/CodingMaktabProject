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
        r.screenshot("./file_radio1.png")
    else:
        r.click()
        r.screenshot("./file_radio2.png")

# take the screenshot
driver.save_screenshot("./fullpage.png")

driver.close()