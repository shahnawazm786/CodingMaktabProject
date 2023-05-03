from selenium.webdriver.common.by import By

class LoginPage:
    inputUserTextBox_Name='By.NAME'
    inputPasswordTextBox_By_Name='password'
    btnLogin_By_Xpath="//button[@type='submit']"
    imgLogo_By_Xpath="(//img)[1]"

    def __init__(self,driver):
        self.driver=driver

    def enterUserName(self,username):
        self.driver.find_element(By.NAME,self.inputUserTextBox_Name).clear()
        self.driver.find_element(By.NAME,self.inputUserTextBox_Name).send_keys(username)

    def enterPassword(self,password):
        self.driver.find_element(By.NAME,self.inputPasswordTextBox_By_Name).clear()
        self.driver.find_element(By.NAME,self.inputPasswordTextBox_By_Name).send_keys(password)

    def loginButtonClick(self):
        self.driver.find_element(By.XPATH,self.btnLogin_By_Xpath).click()








