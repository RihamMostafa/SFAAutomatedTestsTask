# driver_setup.py

from appium import webdriver
from configs.config_ import Config

class DriverSetup:
    def __init__(self, platform):
 
        if platform.lower() == 'android':
            self.desired_caps = Config.ANDROID
        elif platform.lower() == 'ios':
            self.desired_caps = Config.IOS
        else:
            raise ValueError("Platform must be either 'android' or 'ios'")
        
        self.driver = None

    def start_driver(self):

        self.driver = webdriver.Remote(Config.APPIUM_SERVER_URL, self.desired_caps)
        #self.driver.activate_app("com.uxbert.sfa")
        self.driver.implicitly_wait(5)
        #print("Driver initialized:", self.driver)  # Log driver status

        return self.driver

    def stop_driver(self):
 
        if self.driver:
            self.driver.quit()
