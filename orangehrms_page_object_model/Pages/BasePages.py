from selenium.webdriver.common.by import By
from selenium import webdriver
class BasePage:
    @classmethod
    def setup(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)
        self.driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")

    @classmethod
    def tearup(self):
        self.driver.delete_all_cookies()
        self.driver.quit()
        self.driver.close()