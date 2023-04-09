from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class selenium_common_function:

    @classmethod
    def waitTillLoading(cls,driver,element,duration):
        return WebDriverWait(driver=driver,duration=duration,poll_frequency=2).until(
            expected_conditions.visibility_of(element))

    @classmethod
    def waitTillElementClickable(cls,driver,val,duration):
        return WebDriverWait(driver,duration).until(
                expected_conditions.element_to_be_clickable(By.XPATH,value=val))



