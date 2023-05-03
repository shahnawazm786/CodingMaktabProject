from selenium.webdriver.common.by import By

class LoginPage:
    inputUserTextBox=By.NAME(value="username")
    inputPasswordTextBox=By.NAME(value="password")
    btnLogin=By.XPATH(value="//button[@type='submit']")
    imgLogo=By.XPATH(value="(//img)[1]")

    def __init__(self,driver):
        self.driver=driver

    def enterUserName(self,username):
        self.driver.find_element(self.inputUserTextBox).clear()
        self.driver.find_element(self.inputUserTextBox).send_keys(username)

    def enterPassword(self,password):
        self.driver.find_element(self.inputPasswordTextBox).clear()
        self.driver.find_element(self.inputPasswordTextBox).send_keys(password)

    def loginButtonClick(self):
        self.driver.find_element(self.btnLogin).click()








