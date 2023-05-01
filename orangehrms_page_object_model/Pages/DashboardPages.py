from selenium.webdriver.common.by import By
from selenium import webdriver
from BasePages import BasePage
class Dashboard(BasePage):
    headerLevel=By.XPATH(value="//h6")
    searchTextBox=By.CSS_SELECTOR(value="input[class='oxd-input oxd-input--active']")
    adminLink=By.XPATH(value="//span[text()='Admin']//..")

    def clickOnAdminLink(self):
        self.driver.find_element(self.adminLink).click()



