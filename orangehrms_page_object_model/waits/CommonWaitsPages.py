from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
class WaitsDriver:
    def __init__(self,driver):
        self.driver=driver

    def wait_element_to_be_clickable(self,locator):
        self.wait=WebDriverWait(self.driver,10)
        return self.wait.until(EC.element_to_be_clickable(locator))
    def wait_visibility_of_element_located(self,locator):
        self.wait=WebDriverWait(self.driver,10)
        return self.wait.until(EC.invisibility_of_element_located(locator))


