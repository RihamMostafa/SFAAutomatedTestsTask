from pages.base_page import BasePage
from resources.ProfilePageLocators import ProfilePageLocatorsEN

class ProfilePage(BasePage):
    
    locators= ProfilePageLocatorsEN
    
    def changeLanguageToEnglish(self):
        self.click_element(self.locators.settingsIcone)
        self.click_element(self.locators.changeLanguageBtn)
        self.click_element(self.locators.toEnglishBtn)
        
    def changeLanguageToArabic(self):
        self.click_element(self.locators.settingsIcone)
        self.click_element(self.locators.changeLanguageBtn)
        self.click_element(self.locators.toArabicBtn)
    
    def confirmChangingLanguageToArabic(self):
        self.click_element(self.locators.yesArAlertBtn)
    
    def denyChangingLanguageToArabic(self):
        self.click_element(self.locators.noArAlertBtn)
