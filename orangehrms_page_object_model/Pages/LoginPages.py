from selenium.webdriver.common.by import By

class LoginPage:
    inputUserTextBox=By.NAME("username")
    inputPasswordTextBox=By.NAME("password")
    btnLogin=By.XPATH("//button[@type='submit']")
    imgLogo=By.XPATH("(//img)[1]")

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








