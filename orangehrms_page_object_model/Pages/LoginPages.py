from selenium.webdriver.common.by import By

class LoginPage:
    user_name_input_box_by_name="username"
    text_passsword_by_name="password"
    btn_login_by_xpath="//button[@type='submit']"
    imgLogo_By_Xpath="(//img)[1]"

    def __init__(self,driver):
        self.driver=driver

    def setUserName(self,username):
        print(username)
        self.driver.find_element(By.NAME,self.user_name_input_box_by_name).clear()
        self.driver.find_element(By.NAME,self.user_name_input_box_by_name).send_keys(username)

    def setPassword(self,password):
        print(password)
        self.driver.find_element(By.NAME,self.text_passsword_by_name).clear()
        self.driver.find_element(By.NAME,self.text_passsword_by_name).send_keys(password)

    def clickLoginButton(self):
        self.driver.find_element(By.XPATH,self.btn_login_by_xpath).click()
        print('clicked')








