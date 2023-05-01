from selenium.webdriver.common.by import By
from selenium import webdriver
from  BasePages import BasePage
class LoginPage(BasePage):
    inputUserTextBox=By.NAME(value="username")
    inputPasswordTextBox=By.NAME(value="password")
    btnLogin=By.XPATH(value="//button[@type='submit']")
    imgLogo=By.XPATH(value="(//img)[1]")



    def enterUserName(self):
        self.driver.find_element(self.inputUserTextBox).clear()
        self.driver.find_element(self.inputUserTextBox).send_keys("Admin")

    def enterPassword(self):
        self.driver.find_element(self.inputPasswordTextBox).clear()
        self.driver.find_element(self.inputPasswordTextBox).send_keys("admin123")

    def loginButtonClick(self):
        self.driver.find_element(self.btnLogin).click()








