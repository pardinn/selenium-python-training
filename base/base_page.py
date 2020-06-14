""" @package

Base Page class implementation
It implements methods which are common to all pages throughout the application

This class needs to be inherited by all the page classes
This should not be used by creating object instances

Examples:
    Class LoginPage(BasePage)
"""
from base.selenium_driver import SeleniumDriver
from traceback import print_stack
from utilities.util import Util
import time


class BasePage(SeleniumDriver):

    _loading = ".nprogress-busy"

    def __init__(self, driver):
        """ Inits BasePage class """
        super().__init__(driver)
        self.driver = driver
        self.util = Util()

    def verify_page_title(self, expected_title):
        """ Verify the page Title is as expected

        :param expected_title: the text to verfify
        :return: True or False
        """
        try:
            actual_title = self.get_title()
            return self.util.verify_text_contains(actual_title, expected_title)
        except:
            self.log.error("Failed to get page title")
            print_stack()
            return False

    def wait_for_page_load(self):
        time.sleep(1)
        self.wait_for_element_invisibility(self._loading, "xpath")
