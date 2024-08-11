import pytest
from pages.navigation_bar import NavigationBar
from tests.test_base import BaseTest


@pytest.mark.usefixtures("setup_class","pass_welcome_screen","skip_tutorial")
class TestNavigationBar(BaseTest):
    
    
    @pytest.mark.xfail
    def test_NavigateToDiscover(self):
        
        navigationBar= NavigationBar(self.driver)
        navigationBar.navigateToDiscover()
        assert navigationBar.is_displayed(navigationBar.navigationBarLocators.discoverButton)
        assert navigationBar.is_enabled(navigationBar.navigationBarLocators.discoverButton)
        assert navigationBar.is_selected(navigationBar.get_parent_locator(navigationBar.navigationBarLocators.discoverButton))
        assert navigationBar.get_text(navigationBar.navigationBarLocators.discoverButton) == 'Discover'
        
    @pytest.mark.xfail
    def test_NavigateToGroups(self):
        
        navigationBar= NavigationBar(self.driver)
        navigationBar.navigateToGroups()
        assert navigationBar.is_displayed(navigationBar.navigationBarLocators.groupsButton)
        assert navigationBar.is_enabled(navigationBar.navigationBarLocators.groupsButton)
        assert navigationBar.is_selected(navigationBar.get_parent_locator(navigationBar.navigationBarLocators.groupsButton))
        assert navigationBar.get_text(navigationBar.navigationBarLocators.groupsButton) == 'Groups'
    
    @pytest.mark.xfail
    def test_NavigateToOrganization(self):
        
        navigationBar= NavigationBar(self.driver)
        navigationBar.navigateToOrganization()
        assert navigationBar.is_displayed(navigationBar.navigationBarLocators.organizationButton)
        assert navigationBar.is_enabled(navigationBar.navigationBarLocators.organizationButton)
        assert navigationBar.is_selected(navigationBar.get_parent_locator(navigationBar.navigationBarLocators.organizationButton))
        assert navigationBar.get_text(navigationBar.navigationBarLocators.organizationButton) == 'Organization'
        pass

    @pytest.mark.xfail
    def test_NavigateToEvents(self):
        
        navigationBar= NavigationBar(self.driver)
        navigationBar.navigateToEventsTab()
        assert navigationBar.is_displayed(navigationBar.navigationBarLocators.eventsButton)
        assert navigationBar.is_enabled(navigationBar.navigationBarLocators.eventsButton)
        assert navigationBar.is_selected(navigationBar.get_parent_locator(navigationBar.navigationBarLocators.eventsButton))
        assert navigationBar.get_text(navigationBar.navigationBarLocators.eventsButton) == 'Events'

    @pytest.mark.xfail
    def test_NavigateToProfile(self):
        
        navigationBar= NavigationBar(self.driver)
        navigationBar.navigateToProfileTab()
        assert navigationBar.is_displayed(navigationBar.navigationBarLocators.profileButton)
        assert navigationBar.is_enabled(navigationBar.navigationBarLocators.profileButton)
        assert navigationBar.is_selected(navigationBar.get_parent_locator(navigationBar.navigationBarLocators.profileButton))
        assert navigationBar.get_text(navigationBar.navigationBarLocators.profileButton) == 'Profile'

