from selenium import webdriver
import time

from selenium.common import NoSuchElementException, ElementNotVisibleException, ElementNotSelectableException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

driver=webdriver.Chrome()
driver.implicitly_wait(5)
#driver.get('file:///C:/files/index.html')
driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
#ele=driver.find_element(By.NAME,value="q")
#ele.send_keys("KAZ - IT training Hub")
#ele=driver.find_element(By.TAG_NAME,value="p")
#print(ele.text)
#time.sleep(5)

#Expilcit -> WebDriverWait & FluentWait
WebDriverWait(driver, timeout=20,ignored_exceptions=NoSuchElementException).until(
    expected_conditions.visibility_of(driver.find_element(By.NAME,value="username"))
)
WebDriverWait(driver, timeout=20,ignored_exceptions=NoSuchElementException).until(
    expected_conditions.visibility_of(driver.find_element(By.NAME,value="password"))
)
WebDriverWait(driver, timeout=20,ignored_exceptions=NoSuchElementException).until(
    expected_conditions.visibility_of(driver.find_element(By.TAG_NAME,value="button"))
)

ele=driver.find_element(By.NAME,value="username")
ele1=driver.find_element(By.NAME,value="password")
btn=driver.find_element(By.TAG_NAME,value="button")
ele.send_keys("1234567")
ele1.send_keys("abc")
btn.click()
# Fluent Wait
wait = WebDriverWait(driver,
                     timeout=10,
                     poll_frequency=1,
                     ignored_exceptions=[ElementNotVisibleException, ElementNotSelectableException])
element = wait.until(expected_conditions.element_to_be_clickable((By.XPATH, "//p[text()='Invalid credentials']")))
msg=driver.find_element(By.XPATH,value="//p[text()='Invalid credentials']")
assert msg.is_displayed() == True
time.sleep(5)
driver.close()