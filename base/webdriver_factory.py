""" @package base

WebDriver Factory class implementation
It creates a webdriver instance based on browser configurations

Example:
    wdf = WebDriverFactory(browser)
    wdf.get_web_driver_instance()
"""
from selenium import webdriver
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.microsoft import IEDriverManager


class WebDriverFactory():

    def __init__(self, browser):
        """ Inits WebDriverFactory class

        :returns None
        """
        self.browser = browser

    def get_webdriver_instance(self):
        """ Get WebDriver Instance based on the browser configuration

        :returns 'WebDriver Instance'
        """
        if self.browser == "iexplorer":
            driver = webdriver.Ie(IEDriverManager().install())
        elif self.browser == "firefox":
            driver = webdriver.Firefox(
                executable_path=GeckoDriverManager().install())
        elif self.browser == "chrome":
            driver = webdriver.Chrome(ChromeDriverManager().install())
        else:
            driver = webdriver.Chrome(ChromeDriverManager().install())

        # driver.implicitly_wait(3)
        driver.maximize_window()
        driver.get("https://letskodeit.teachable.com/")
        return driver
