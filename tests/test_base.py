import pytest
from utils.driver_setup import DriverSetup
from configs.config_ import Config
from pages.tutorial_page import TutorialPage
from pages.welcome_page import WelcomePage


class BaseTest:
    driver = None

    @pytest.fixture(scope="class")
    def setup_class(self, request):
        
        print("Running setup_class")
        
        driver_setup = DriverSetup("Android")
        driver_setup.start_driver()
        self.driver = driver_setup.driver

        # Make the driver available in test methods
        request.cls.driver = self.driver

        yield
        self.driver.quit()
    
    @pytest.fixture(scope="class")
    def pass_welcome_screen(self):
        
        print("Running pass_welcome_screen")
        welcome_page_obj= WelcomePage(self.driver)
        try:
            welcome_page_obj.clickContinue()
    
        except Exception as e:
            pytest.fail(f"Failed to pass welcome screen: {e}")
    
    @pytest.fixture(scope="class")
    def skip_tutorial(self):
        
        print("Running skip_tutorial")
        tutorial_page_obj= TutorialPage(self.driver)
        try:
            tutorial_page_obj.clickSkip()
        except Exception as e:
            pytest.fail(f"Failed to skip tutorial: {e}")
    
