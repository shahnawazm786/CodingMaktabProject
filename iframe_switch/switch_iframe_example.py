from selenium import webdriver
import time

from selenium.webdriver.common.by import By
driver=webdriver.Chrome()
driver.implicitly_wait(5)
driver.get('https://www.jqueryscript.net/tags.php?/event%20calendar/')