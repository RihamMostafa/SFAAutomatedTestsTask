from pages.base_page import BasePage
from resources.TutorialLocators import TutorialLocatorsAr , TutorialLocatorsEn
from configs.config_ import Config

class TutorialPage(BasePage):
    
    locators= TutorialLocatorsEn if Config.LOCALE == "EN" else TutorialLocatorsAr
    
    def clickStart(self):
        self.click_element(self.locators.startButton)
        
    def clickSkip(self):
        self.click_element( self.locators.skipButton)
    