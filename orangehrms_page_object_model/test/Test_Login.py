from selenium import webdriver
from orangehrms_page_object_model.Pages.LoginPages import LoginPage
from pytest_html_reporter import attach
import pytest_html
import time
class Test001_Login:
    baseURL='https://opensource-demo.orangehrmlive.com/web/index.php/auth/login'
    userName='Admin'
    password='admin123'

    def test_home_page_title(self,setup):
        #self.driver=webdriver.Chrome()
        self.driver=setup
        self.driver.implicitly_wait(10)
        self.driver.get(self.baseURL)
        self.driver.maximize_window()
        time.sleep(10)
        page_title=self.driver.title
        print(page_title)

        if page_title == 'OrangeHRM123':
            assert True
            self.driver.close()
        else:
            #attach(self.driver.get_screenshot_as_file("test_home_page_title.png"))
            #self.driver.get_screenshot_as_png()
            #self.driver.get_screenshot_as_file("1.png")
            self.driver.save_screenshot("test_home_page_title.png")
            self.driver.close()
            assert False


    def test_login_to_job_portal(self,setup):
        #self.driver=webdriver.Chrome()
        self.driver = setup
        self.driver.implicitly_wait(10)
        self.driver.get(self.baseURL)
        self.driver.maximize_window()
        self.login_page=LoginPage(self.driver)
        self.login_page.setUserName(self.userName)
        self.login_page.setPassword(self.password)
        self.login_page.clickLoginButton()
        #self.driver.save_screenshot("test_login_to_job_portal.png")
        self.driver.close()

    def test_logout_from_job_protal(self,setup):
        self.driver=setup







