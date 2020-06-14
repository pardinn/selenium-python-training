""" @package utilities

CheckPoint class implementation
It provides functionality to assert the result of the test execution

Example:
    self.verification.mark_final("Test Name", result, "Message")
"""
from base.selenium_driver import SeleniumDriver
import utilities.custom_logger as cl
import logging


class CheckPoint(SeleniumDriver):
    log = cl.custom_logger(logging.INFO)

    def __init__(self, driver):
        """ Inits TestStatus class """
        super().__init__(driver)
        self.result_list = []

    def set_result(self, result, result_message):
        try:
            if result is not None:
                if result:
                    self.result_list.append("PASS")
                    self.log.info(
                        "# VERIFICATION SUCCESSFUL: " + result_message)
                else:
                    self.result_list.append("FAIL")
                    self.log.error("# VERIFICATION FAILED : " + result_message)
                    self.take_screenshot(result_message)
            else:
                self.result_list.append("FAIL")
                self.log.error("# VERIFICATION FAILED : " + result_message)
                self.take_screenshot(result_message)

        except:
            self.result_list.append("FAIL")
            self.log.error("# EXCEPTION OCCURRED !!!")
            self.take_screenshot(result_message)

    def mark(self, result, result_message):
        """ Mark the result of the verification point in a test case """
        self.set_result(result, result_message)

    def mark_final(self, test_name, result, result_message):
        """ Mark the final result of the verification point in a test case
        This needs to be called at least once in a test case
        This should be final test status of the test case
        """
        self.set_result(result, result_message)
        if "FAIL" in self.result_list:
            self.log.error("### %s : TEST FAILED" % test_name)
            self.result_list.clear()
            assert False
        else:
            self.log.info("### %s : TEST SUCCESSFUL" % test_name)
            self.result_list.clear()
            assert True
