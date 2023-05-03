
from selenium.webdriver.common.by import By
class HomePage:
    link_home_by_xpath="//li[@id='menu-item-1254']/a"
    link_about_by_xpath="//li[@id='menu-item-1255']/a"
    link_my_account_by_xpath="//li[@id='menu-item-1256']/a"
    link_cart_by_xpath="//li[@id='menu-item-1257']/a"
    link_contact_us_by_xpath="//li[@id='menu-item-1258']/a"
    header_text_by_xpath="//h2[text()='Blue Shoes']"

    def __init__(self,driver):
        self.driver=driver
    def click_on_home_link(self):
        self.driver.find_element(By.XPATH,self.link_home_by_xpath).click()
    def click_on_about_link(self):
        self.driver.find_element(By.XPATH, self.link_about_by_xpath).click()
    def click_on_my_account_link(self):
        self.driver.find_element(By.XPATH, self.link_my_account_by_xpath).click()
    def click_on_cart_lin(self):
        self.driver.find_element(By.XPATH, self.link_cart_by_xpath).click()
    def click_on_contact_us_link(self):
        self.driver.find_element(By.XPATH, self.link_contact_us_by_xpath).click()
    def verify_header_of_item(self,header):
        actual_header=self.driver.find_element(By.XPATH,self.header_text_by_xpath).get_text()
        if actual_header == header:
            assert True
        else:
            assert False

    def verify_home_page_title(self,title):
        if title == 'AskOmDch – Become a Selenium automation expert!':
            assert True
        else:
            assert False
