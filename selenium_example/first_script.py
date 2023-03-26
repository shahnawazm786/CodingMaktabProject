from selenium import webdriver

driver=webdriver.Chrome()
#driver.get("https://www.google.com")
driver.get("https://www.selenium.dev/selenium/web/web-form.html")
for i in range(1,100000000):
    pass
driver.quit()