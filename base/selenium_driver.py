import logging
from traceback import print_stack
from selenium.common.exceptions import *
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.select import Select
import utilities.custom_logger as cl
import time
import os


class SeleniumDriver():
    log = cl.custom_logger(logging.DEBUG)

    def __init__(self, driver):
        self.driver = driver

    def take_screenshot(self, result_message):
        """ Takes screenshot of the current open web page """
        file_name = "%s.%s.png" % (
            result_message, str(round(time.time() * 1000)))
        screenshot_directory = os.path.join(os.curdir, "screenshots")
        relative_file_name = os.path.join(screenshot_directory, file_name)
        destination_file = os.path.abspath(relative_file_name)
        destination_directory = os.path.abspath(screenshot_directory)
        try:
            if not os.path.exists(destination_directory):
                os.makedirs(destination_directory)
            self.driver.save_screenshot(destination_file)
            self.log.info("Screenshot saved to directory: " + destination_file)
        except:
            self.log.error("### Exception Occurred")
            print_stack()

    def get_title(self):
        return self.driver.title

    def get_by_type(self, locator_type):
        locator_type = locator_type.lower()
        switcher = {
            "id": By.ID,
            "name": By.NAME,
            "xpath": By.XPATH,
            "css": By.CSS_SELECTOR,
            "class": By.CLASS_NAME,
            "link": By.LINK_TEXT,
            "tag": By.TAG_NAME
        }
        return switcher.get(locator_type, False)

    def get_element(self, locator, locator_type="id", wait=True):
        element = None
        try:
            locator_type = locator_type.lower()
            by_type = self.get_by_type(locator_type)
            if wait:
                return self.wait_for_element(locator, locator_type)
            element = self.driver.find_element(by_type, locator)
            # self.log.info("Element found with locator: %s, locatorType: %s" % (
            #     locator, locator_type))
        except:
            self.log.error(
                "Element not found with locator: %s, locatorType: %s" % (
                    locator, locator_type))
        return element

    def get_element_list(self, locator, locator_type="id"):
        """ Get list of elements """
        element = None
        try:
            locator_type = locator_type.lower()
            by_type = self.get_by_type(locator_type)
            element = self.driver.find_elements(by_type, locator)
            # self.log.info(
            #     "Element list found with locator: %s, locatorType: %s" % (
            #         locator, locator_type))
        except:
            self.log.error(
                "Element list not found with locator: %s, locatorType: %s" % (
                    locator, locator_type))
        return element

    def click_element(self, locator="", locator_type="id", element=None):
        """
        Click on an element

        :Args:
        - locator: the identification of the web element
        - locator_type: the By type
        - element: the webelement itself

        :Usage:
            driver.click_element('locator')
            driver.click_element('locator', 'xpath')
            driver.click_element(element=my_element)
        """
        try:
            if locator:
                element = self.get_element(locator, locator_type)
            element.click()
            self.log.info(
                "Clicked on element with locator: %s, locatorType: %s" % (
                    locator, locator_type))
        except:
            self.log.error(
                "Cannot click on element with locator: %s, locatorType: %s" % (
                    locator, locator_type))
            print_stack()

    def send_keys(self, data, locator="", locator_type="id", element=None):
        try:
            if locator:
                element = self.get_element(locator, locator_type)
            element.send_keys(data)
            self.log.info(
                "Sent data to element with locator: %s, locatorType: %s" % (
                    locator, locator_type))
        except:
            self.log.error(
                "Cannot send data to element with locator: %s, locatorType: %s"
                % (locator, locator_type))
            print_stack()

    def send_keys_with_delay(self, data, locator="", locator_type="id",
                             element=None, secs: float = 0.005):
        """
        Adds a delay of n seconds to enter each key

        Args:
            data: text to be entered
            locator: the locator of the element to receive the text
            locator_type: By text (id(default), xpath, link, class, etc)
            element: use it to pass the webelement instead of locator and type

        Returns:
            None
        """
        try:
            if locator:
                element = self.get_element(locator, locator_type)
            for letter in data:
                element.send_keys(letter)
                time.sleep(secs)
            self.log.info(
                "Sent data to element with locator: %s, locatorType: %s" % (
                    locator, locator_type))
        except:
            self.log.error(
                "Cannot send data to element with locator: %s, locatorType: %s"
                % (locator, locator_type))
            print_stack()

    def get_text(self, locator="", locator_type="id", element=None, info=""):
        """
        Get 'Text' on an element
        Either provide element or a combination of locator and locator_type
        """
        try:
            if locator:
                self.log.debug("In locator condition")
                element = self.get_element(locator, locator_type)
            self.log.debug("Before finding text")
            text = element.text
            self.log.debug("After finding element, size is:" + str(len(text)))
            if len(text) == 0:
                text = element.get_attribute("innerText")
            if len(text) != 0:
                self.log.info("Getting text on element :: " + info)
                self.log.info("The text is :: '%s'" % text)
                text = text.strip()
        except:
            self.log.error("Failed to get txt on element " + info)
            print_stack()
            text = None

    def is_element_present(self, locator="", locator_type="id", element=None,
                           wait=True):
        """
        Check if element is present
        Either provide element or a combination of locator and locator_type
        """
        try:
            if locator:
                element = self.get_element(locator, locator_type, wait=wait)
            if element is not None:
                self.log.info(
                    "Element present with locator: %s, locatorType: %s" % (
                        locator, locator_type))
                return True
            else:
                self.log.info(
                    "Element not present with locator: %s, locatorType: %s" % (
                        locator, locator_type))
                return False
        except:
            self.log.error(
                "Element not found with locator: %s, locatorType: %s" % (
                    locator, locator_type))
            return False

    def is_element_displayed(self, locator="", locator_type="id",
                             element=None):
        """
        Check if element is displayed
        Either provide element or a combination of locator and locator_type
        """
        is_displayed = False
        try:
            if locator:
                element = self.get_element(locator, locator_type)
            if element is not None:
                is_displayed = element.is_displayed()
                self.log.info(
                    "Element is displayed with locator: %s, locator_type: %s"
                    % (locator, locator_type))
            else:
                self.log.info(
                    "Element not displayed with locator: %s, locator_type: %s"
                    % (locator, locator_type))
            return is_displayed
        except:
            self.log.error(
                "Element not found with locator: %s, locatorType: %s" % (
                    locator, locator_type))
            return False

    def elements_presence_check(self, locator, by_type):
        try:
            elements_list = self.driver.find_elements(by_type, locator)
            if len(elements_list) > 0:
                self.log.info("Element found with locator: %s, locatorType: %s"
                              % (locator, by_type))
                return True
            else:
                self.log.error(
                    "Element not found with locator: %s, locatorType: %s" % (
                        locator, by_type))
                return False
        except:
            self.log.error(
                "Element not found with locator: %s, locatorType: %s" % (
                    locator, by_type))
            return False

    def wait_for_element(self, locator, locator_type="id",
                         timeout=10, poll_frequency=0.5):
        element = None
        try:
            by_type = self.get_by_type(locator_type)
            self.log.info("Waiting for maximum :: " + str(timeout) +
                          " :: seconds for element to be clickable")
            wait = WebDriverWait(self.driver, timeout, poll_frequency,
                                 ignored_exceptions=[NoSuchElementException,
                                                     ElementNotVisibleException,
                                                     ElementNotSelectableException])

            element = wait.until(
                EC.element_to_be_clickable((by_type, locator)))
            self.log.info("Element appeared on the web page")
        except:
            self.log.error("Element did not appear on the web page")
            print_stack()
        return element

    def wait_for_element_invisibility(self, locator, locator_type="id",
                                      timeout=10, poll_frequency=0.5):
        element = None
        try:
            by_type = self.get_by_type(locator_type)
            self.log.info(
                "Waiting for maximum %s seconds for element to be invisible"
                % str(timeout))
            wait = WebDriverWait(self.driver, timeout, poll_frequency,
                                 ignored_exceptions=[NoSuchElementException,
                                                     ElementNotVisibleException,
                                                     ElementNotSelectableException])

            element = wait.until(
                EC.invisibility_of_element((by_type, locator)))
            self.log.info("Element disappeared from the web page")
        except:
            self.log.error("Element did not disappear from the web page")
            print_stack()
        return element

    def wait_for_elements(self, locator, locator_type="id",
                          timeout=10, poll_frequency=0.5):
        elements = None
        try:
            by_type = self.get_by_type(locator_type)
            self.log.info(
                "Waiting for maximum %s seconds for elements to be clickable"
                % str(timeout))
            wait = WebDriverWait(self.driver, timeout, poll_frequency,
                                 ignored_exceptions=[NoSuchElementException,
                                                     ElementNotVisibleException,
                                                     ElementNotSelectableException])

            elements = wait.until(
                EC.presence_of_all_elements_located((by_type, locator)))
            self.log.info("Elements appeared on the web page")
        except:
            self.log.error("Elements did not appear on the web page")
            print_stack()
        return elements

    def web_scroll(self, direction="up"):
        if direction == "up":
            self.driver.execute_script("window.scrollBy(0, -600);")
        if direction == "down":
            self.driver.execute_script("window.scrollBy(0, 600);")

    def switch_to_dynamic_frame(self, locator, locator_type="id"):
        """
        Switch to iFrame by index after finding element locator inside it
        Args:
            locator: locator of the element to be found inside iframe
            locator_type: locator type of the element to be found

        Returns:
            Index of iFrame
        """
        index = None
        try:
            iframe_list = self.get_element_list("iframe", "tag")
            self.log.info("Length of iFrame list: " + str(len(iframe_list)))
            for i in range(len(iframe_list)):
                self.switch_to_frame(iframe_list[i])
                if self.is_element_present(locator, locator_type, wait=False):
                    index = i
                    self.log.info(
                        "Found element on iframe index is: " + str(i))
                    break
                self.switch_to_default_content()
            return index
        except:
            self.log.error("Unable to switch to iFrame. Element not found")
            return index

    def switch_to_frame(self, frame_reference=None):
        """
        Switches focus to the specified frame, by index, name, or webelement.

        :Args:
         - frame_reference: The name of the window to switch to,
                            an integer representing the index,
                            or a webelement that is an (i)frame to switch to.

        :Usage:
            driver.switch_to.frame('frame_name')
            driver.switch_to.frame(1)
            driver.switch_to.frame(driver.find_elements_by_tag_name("iframe")[0])
        """
        self.driver.switch_to.frame(frame_reference)

    def switch_to_default_content(self):
        """
        Switch focus to the default frame.

        :Usage:
            driver.switch_to.default_content()
        """
        self.driver.switch_to.default_content()

    def select_by_visible_text(self, data, locator="", locator_type="id",
                               element=None):
        try:
            if locator:
                element = self.get_element(locator, locator_type)
            sel = Select(element)
            sel.select_by_visible_text(data)
            self.log.info("Selected option: %s" % data)
        except:
            self.log.error("Option %s is not valid" % data)

    def get_attribute(self, attribute, locator="",
                      locator_type="id", element=None):
        """
        Get value of the attribute of element

        :Args:
            attribute: attribute whose value to find
            locator: locator of the element
            locator_type: locator type to find the element
            element: element whose attribute need to be found

        :Returns:
            Value of attribute

        Usage:
            driver.get_element_attribute_value("class", "my_locator", "id")
            driver.get_element_attribute_value("class", "my_locator")
            driver.get_element_attribute_value("class", element=my_element)
        """
        try:
            if locator:
                element = self.get_element(locator, locator_type)
            return element.get_attribute(attribute)
        except:
            self.log.error(
                "Unable to retrieve %s of element with locator '%s', "
                "locatorType '%s'" % (
                    attribute, locator, locator_type))

    def is_enabled(self, locator, locator_type="id", info=""):
        """
        Check if element is enabled

        Args:
            locator: locator of the element to check
            locator_type: type of the locator(id(default), xpath, css, class, link)
            info: information about the element, label/name of the element

        Returns:
            True or False
        """
        element = self.get_element(locator, locator_type=locator_type)
        enabled = False
        try:
            attribute_value = self.get_attribute(element=element,
                                                 attribute="disabled")
            if attribute_value is not None:
                enabled = element.is_enabled()
            else:
                value = self.get_attribute(element=element, attribute="class")
                self.log.info(
                    "Attribute value from application Web UI -> " + value)
                enabled = not ("disabled" in value)
            if enabled:
                self.log.info("Element :: '%s' is enabled" % info)
            else:
                self.log.info("Element :: '%s' is not enabled" % info)
        except:
            self.log.error("Element :: '%s' state could not be found" % info)
        return enabled
