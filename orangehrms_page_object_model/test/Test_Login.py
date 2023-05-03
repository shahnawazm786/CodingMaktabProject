from selenium import webdriver
from orangehrms_page_object_model.Pages.LoginPages import LoginPage
class Test001_Login:
    baseURL='https://opensource-demo.orangehrmlive.com/web/index.php/auth/login'
    userName='Admin'
    password='admin123'

    def test_home_page_title(self):
        self.driver=webdriver.Chrome()
        self.driver.implicitly_wait(10)
        self.driver.get(self.baseURL)
        self.driver.maximize_window()
        page_title=self.driver.title
        self.driver.quit()
        self.driver.close()
        if page_title=='OrangeHRM':
            assert True
        else:
            assert False

    def test_login_to_job_portal(self):
        self.driver=webdriver.Chrome()
        self.driver.implicitly_wait(10)
        self.driver.get(self.baseURL)
        self.driver.maximize_window()
        self.login_page=LoginPage(self.driver)
        self.login_page.setUserName(self.userName)
        self.login_page.setPassword(self.password)
        self.login_page.loginButtonClick()
        self.driver.quit()
        self.driver.close()






