from base.base_page import BasePage
from pages.home.navigation_page import NavigationPage
import utilities.custom_logger as cl
import logging


class LoginPage(BasePage):
    log = cl.custom_logger(logging.DEBUG)

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.nav = NavigationPage(driver)

    # Locators
    _login_link = "Login"
    _email_field = "user_email"
    _password_field = "user_password"
    _login_button = "commit"
    _logout_button = "Log Out"

    def click_login_link(self):
        self.click_element(self._login_link, "link")

    def enter_email(self, email):
        self.send_keys(email, self._email_field)

    def enter_password(self, password):
        self.send_keys(password, self._password_field)

    def click_login_button(self):
        self.click_element(self._login_button, "name")

    def login(self, email="", password="", click_login=True):
        if click_login:
            self.click_login_link()
        self.clear_fields()
        self.enter_email(email)
        self.enter_password(password)
        self.click_login_button()

    def verify_login_successful(self):
        result = self.is_element_present(
            "//*[@id='navbar']//img[@class='gravatar']", "xpath")
        return result

    def verify_login_failed(self):
        result = self.is_element_present(
            "//div[contains(text(),'Invalid email or password')]", "xpath")
        return result

    def clear_fields(self):
        self.get_element(self._email_field).clear()
        self.get_element(self._password_field).clear()

    def verify_login_title(self):
        return self.verify_page_title("Let's Kode It")

    def logout(self):
        self.nav.go_to_user_settings()
        self.click_element(self._logout_button, "link")
