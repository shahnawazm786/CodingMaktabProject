from selenium import webdriver
class Test001_Login:
    baseURL='https://opensource-demo.orangehrmlive.com/web/index.php/auth/login'
    userName='Admin'
    password='admin123'

    def test_home_page_title(self):
        self.driver=webdriver.Chrome()
        self.driver.get(self.baseURL)
        self.driver.implicitly_wait(10)
        page_title=self.driver.title
        if page_title=='OrangeHRM':
            assert True
        else:
            assert False

    def test_login_to_job_portal(self):
        self.driver=webdriver.Chrome()
        self.driver.get(self.baseURL)
        login_page




