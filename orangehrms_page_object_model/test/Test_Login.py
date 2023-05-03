from selenium import webdriver
from orangehrms_page_object_model.Pages.LoginPages import LoginPage
import time
class Test001_Login:
    baseURL='https://opensource-demo.orangehrmlive.com/web/index.php/auth/login'
    userName='Admin'
    password='admin123'

    def test_home_page_title(self):
        self.driver=webdriver.Chrome()
        self.driver.implicitly_wait(10)
        self.driver.get(self.baseURL)
        self.driver.maximize_window()
        time.sleep(10)
        page_title=self.driver.title
        print(page_title)
        if page_title == 'OrangeHRM':
            assert True
        else:
            assert False
        time.sleep(10)
        self.driver.quit()
        self.driver.close()
    def test_login_to_job_portal(self):
        self.driver=webdriver.Chrome()
        self.driver.implicitly_wait(10)
        self.driver.get(self.baseURL)
        self.driver.maximize_window()
        self.login_page=LoginPage(self.driver)
        self.login_page.setUserName(self.userName)
        self.login_page.setPassword(self.password)
        self.login_page.clickLoginButton()
        time.sleep(20)
        self.driver.quit()
        self.driver.close()






