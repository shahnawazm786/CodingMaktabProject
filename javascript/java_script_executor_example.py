import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()
driver.implicitly_wait(5)
driver.get('https://pytest-html.readthedocs.io/en/latest/user_guide.html')

#action=ActionChains(driver)
#action.scroll_by_amount(100,1000)
driver.execute_script("window.scrollTo(0,document.body.scrollHeight);")
print(driver.execute_script('return document.title'))
print(driver.execute_script('return document.URL'))
btn=driver.find_element(By.XPATH,value="//a[text()='Changelog']")
driver.execute_script ("arguments[0].click();",btn)
time.sleep(10)
driver.quit()


