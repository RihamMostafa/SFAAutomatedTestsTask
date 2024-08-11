from pages.base_page import BasePage
from resources.NavigationLocators import NavigationLocatorsAr, NavigationLocatorsEn
from configs.config_ import Config

class NavigationBar(BasePage):
    
    def __init__(self, driver):
        super().__init__(driver)
        self.navigationBarLocators = NavigationLocatorsEn if Config.LOCALE== "EN" else NavigationLocatorsAr
    
    def navigateToProfileTab(self):
        self.click_element(self.navigationBarLocators.profileButton)
    
    def navigateToEventsTab(self):
        self.click_element(self.navigationBarLocators.eventsButton)

    def navigateToOrganization(self):
        self.click_element(self.navigationBarLocators.organizationButton)
        
    def navigateToGroups(self):
        self.click_element(self.navigationBarLocators.groupsButton)
    
    def navigateToDiscover(self):
        self.click_element(self.navigationBarLocators.discoverButton)
        
