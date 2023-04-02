from selenium import webdriver

from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By

import time
import pytest
#https://docs.pytest.org/en/7.2.x/
def test_login_successful():

    driver = webdriver.Chrome()
    driver.implicitly_wait(5)
    driver.get('https://opensource-demo.orangehrmlive.com/web/index.php/auth/login')
    user_name=driver.find_element(By.NAME,value="username")
    password=driver.find_element(By.NAME,value="password")
    btn=driver.find_element(By.TAG_NAME,value="button")
    user_name.send_keys("Admin")
    password.send_keys("admin123")
    btn.click()
    assert driver.title=="OrangeHRM"

def test_not_login_successful():

    driver = webdriver.Chrome()
    driver.implicitly_wait(5)
    driver.get('https://opensource-demo.orangehrmlive.com/web/index.php/auth/login')
    user_name=driver.find_element(By.NAME,value="username")
    password=driver.find_element(By.NAME,value="password")
    btn=driver.find_element(By.TAG_NAME,value="button")
    user_name.send_keys("Admin")
    password.send_keys("")
    btn.click()
    assert driver.title==" "
