from selenium import webdriver
import time

driver=webdriver.Chrome(executable_path='C:\PythonProject\CodingMaktabProject\Drivers\chrome\chromedriver.exe')
#driver=webdriver.Firefox()
#driver.get("https://www.google.com")
driver.get("https://www.selenium.dev/selenium/web/web-form.html")
print(driver.title)
print(driver.page_source)
driver.maximize_window()
driver.minimize_window()
driver.fullscreen_window()
time.sleep(5) #dead sleep
driver.quit()