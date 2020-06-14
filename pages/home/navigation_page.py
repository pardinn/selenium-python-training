from base.base_page import BasePage
import utilities.custom_logger as cl
import logging


class NavigationPage(BasePage):
    log = cl.custom_logger(logging.DEBUG)

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators
    _logo = "//a[@class='navbar-brand header-logo']"
    _my_courses = "My Courses"
    _all_courses = "All Courses"
    _practice = "Practice"
    _user_settings_icon = "//a[contains(@class,'open-my-profile-dropdown')]"

    def go_to_main(self):
        self.click_element(self._logo, "xpath")

    def go_to_all_courses(self):
        self.click_element(self._all_courses, "link")

    def go_to_my_courses(self):
        self.click_element(self._my_courses, "link")

    def go_to_practice(self):
        self.click_element(self._practice, "link")

    def go_to_user_settings(self):
        self.click_element(self._user_settings_icon, "xpath")