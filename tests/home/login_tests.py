from pages.home.login_page import LoginPage
from utilities.checkpoint import CheckPoint
import unittest
import pytest
import utilities.custom_logger as cl
import logging


@pytest.mark.usefixtures("oneTimeSetUp", "setUp")
class LoginTests(unittest.TestCase):
    log = cl.custom_logger(logging.DEBUG)

    @pytest.fixture(autouse=True)
    def class_setup(self, oneTimeSetUp):
        self.lp = LoginPage(self.driver)
        self.cp = CheckPoint(self.driver)

    @pytest.mark.run(order=2)
    def test_validLogin(self):
        self.lp.login("test@email.com", "abcabc", False)
        title_check = self.lp.verify_login_title()
        self.cp.mark(title_check, "Title check")
        login_check = self.lp.verify_login_successful()
        self.cp.mark_final("test_validLogin", login_check, "Login check")

    @pytest.mark.run(order=1)
    def test_invalidLogin(self):
        self.lp.logout()
        self.lp.login("test@email.com", "abc123")
        result = self.lp.verify_login_failed()
        self.cp.mark_final("test_invalidLogin", result, "Login check")
