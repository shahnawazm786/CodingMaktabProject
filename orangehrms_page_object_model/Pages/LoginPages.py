from selenium.webdriver.common.by import By
from selenium import webdriver
class LoginPage():
    inputUserTextBox=By.NAME(value="username")
    inputPasswordTextBox=By.NAME(value="password")
    btnLogin=By.XPATH(value="//button[@type='submit']")
    imgLogo=By.XPATH(value="(//img)[1]")

    @classmethod
    def setup(self):
        self.driver=webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)
        self.driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")

    def enterUserName(self):
        self.driver.find_element(self.inputUserTextBox).clear()
        self.driver.find_element(self.inputUserTextBox).send_keys("Admin")

    def enterPassword(self):
        self.driver.find_element(self.inputPasswordTextBox).clear()
        self.driver.find_element(self.inputPasswordTextBox).send_keys("admin123")

    def loginButtonClick(self):
        self.driver.find_element(self.btnLogin).click()

    @classmethod
    def tearup(self):
        self.driver.delete_all_cookies()
        self.driver.quit()
        self.driver.close()






