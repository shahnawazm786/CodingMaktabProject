from selenium import webdriver
from demo_page.Pages.HomePageObject import HomePage
class Test001_Home:
    baseURL="https://askomdch.com/"
    def test_home_page_title(self,setup):
        #self.driver=webdriver.Chrome()
        self.driver=setup
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)
        self.driver.get(self.baseURL)
        actual_title=self.driver.title
        if actual_title=='AskOmDch – Become a Selenium automation expert!12345':
            assert True
            self.driver.close()
        else:
            self.driver.save_screenshot("test_home_page_title.png")
            self.driver.close()
            assert False

    def test_click_on_home_link(self,setup):
        #self.driver = webdriver.Chrome()
        self.driver = setup
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)
        self.driver.get(self.baseURL)
        self.homePage=HomePage(driver=self.driver)
        self.homePage.click_on_home_link()
        self.homePage.verify_home_page_title(self.driver.title)
        self.driver.close()

    def test_click_on_about_lin(self,setup):
        #self.driver=webdriver.Chrome()
        self.driver = setup
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)
        self.driver.get(self.baseURL)
        self.homePage = HomePage(driver=self.driver)
        self.homePage.click_on_about_link()
        self.driver.close()





