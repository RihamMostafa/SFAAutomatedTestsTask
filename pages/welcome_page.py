from pages.base_page import BasePage
from resources.WelcomePageLocators import WelcomePageLocators

class WelcomePage(BasePage):
    
    locators= WelcomePageLocators
    
    def changeLanguage(self):
        self.click_element(self.locators.languageButton)
        
    
    def clickContinue(self):
        self.click_element(self.locators.continueButton)
    