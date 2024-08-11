import pytest
from pages.welcome_page import WelcomePage
from tests.test_base import BaseTest
from resources.TutorialLocators import TutorialLocatorsAr,TutorialLocatorsEn
from configs.config_ import Config


@pytest.mark.usefixtures("setup_class")
class TestWelcomePage(BaseTest):

    def test_continue(self):
        assert self.driver is not None
        welcomePage = WelcomePage(self.driver)
        welcomePage.clickContinue()
        
        if (Config.LOCALE.upper() == "EN"): assert welcomePage.is_exist(TutorialLocatorsEn.skipButton)
        else: assert welcomePage.is_exist(TutorialLocatorsAr.skipButton)
