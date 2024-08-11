from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from configs.config_ import Config

class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def find_element(self, locator):
        # try:
        #     return self.driver.find_element(MobileBy.XPATH, locator)
        # except Exception as e:
        #     pytest.fail(f"Failed to find element by XPath: {locator}. Error: {e}")
        try:
            return WebDriverWait(self.driver, Config.TIMEOUT).until(
                EC.visibility_of_element_located((MobileBy.XPATH, locator))
            )
        except TimeoutException:
            raise Exception(f"Element with locator '{locator}' not found")

    def get_parent_locator(self, child_locator):
        return child_locator+"/.."


    def click_element(self, locator):
        element = self.find_element(locator)
        element.click()
        
    def enter_text(self, locator, text):
        element = self.find_element(locator)
        element.send_keys(text)

    def is_clickable(self, locator):
        element = self.find_element(locator)
        return element.is_enabled() and element.is_displayed()

    def is_enabled(self, locator):
        element = self.find_element(locator)
        return element.is_enabled()

    def is_displayed(self, locator):
        element = self.find_element(locator)
        return element.is_displayed()

    def is_selected(self, locator):
        element = self.find_element(locator)
        return element.is_selected()

    def get_text(self, locator):
        element = self.find_element(locator)
        return element.text
    
    def is_element_dismissed_or_not_visible(self, locator):
        try:
            WebDriverWait(self.driver, Config.TIMEOUT).until(
                EC.invisibility_of_element((MobileBy.XPATH, locator))
            )
            return True
        except TimeoutException:
            return False
        except NoSuchElementException:
            return True
        
    def is_exist(self, locator):
        try:
            self.find_element(locator)
            return True
        except NoSuchElementException:
            return False