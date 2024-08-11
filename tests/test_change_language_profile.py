import pytest
from pages.profile_page import ProfilePage
from pages.navigation_bar import NavigationBar
from tests.test_base import BaseTest
from configs.config_ import Config
from resources.NavigationLocators import NavigationLocatorsAr,NavigationLocatorsEn


@pytest.mark.usefixtures("setup_class","pass_welcome_screen","skip_tutorial","navigate_to_ProfileTab")
class TestChangeLanguageProfileTab(BaseTest):
    
    @pytest.fixture(scope="function")
    def navigate_to_ProfileTab(self):
        
        print("Running skip_tutorial")
        navigation_bar= NavigationBar(self.driver)
        try:
            navigation_bar.navigateToProfileTab()
        except Exception as e:
            pytest.fail(f"Failed to skip tutorial: {e}")
    
    @pytest.mark.xfail 
    def test_SwitchLanguageFromEnglishToArabic_confirm(self):
        if Config is "AR": pytest.skip("Skipping this test due to language is alrready arabic.")
        else:
            profileTab= ProfilePage(self.driver)
            profileTab.changeLanguageToArabic()
            profileTab.confirmChangingLanguageToArabic()
            assert profileTab.is_element_dismissed_or_not_visible(profileTab.locators.switchLanguageAlertAr)
            assert profileTab.is_exist(NavigationLocatorsAr.profileButton)
            
            
    def test_SwitchLanguageFromEnglishToArabic_deny(self):
        if Config is "AR": pytest.skip("Skipping this test due to language is alrready arabic.")
        else:
            profileTab= ProfilePage(self.driver)
            profileTab.changeLanguageToArabic()
            profileTab.denyChangingLanguageToArabic()
            assert profileTab.is_element_dismissed_or_not_visible(profileTab.locators.switchLanguageAlertAr)
            assert profileTab.is_exist(NavigationLocatorsEn.profileButton)
    
         
    def test_SwitchLanguageFromEnglishToEnglish(self):
        if Config is "AR": pytest.skip("Skipping this test due to language is alrready arabic.")
        else:
            profileTab= ProfilePage(self.driver)
            profileTab.changeLanguageToEnglish()
            assert profileTab.is_element_dismissed_or_not_visible(profileTab.locators.languagesList)
            assert profileTab.is_exist(NavigationLocatorsEn.profileButton)
            
    
            
            
        
        
    