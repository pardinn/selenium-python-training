""" @package utilities

Util class implementation
All most commonly used utilities should be implemented in this class

Example:
    name = self.util.get_unique_name()

"""
import time
import traceback
import random
import string
import utilities.custom_logger as cl
import logging


class Util(object):
    log = cl.custom_logger(logging.INFO)

    def sleep(self, sec, info=""):
        """ Put the program to wait for the specified amount of time """
        if info is not None:
            self.log.info("Wait :: '%s' seconds for %s" % (str(sec), info))
        try:
            time.sleep(sec)
        except InterruptedError:
            traceback.print_stack()

    def get_alpha_numeric(self, length, type="letters"):
        """ Get random string of characters

        :param length: Number of characters string should have
        :param type: Type of characters string should have. Default is letters
                     Provide lower/upper/digits for different types
        :return: a random string
        """
        alpha_num = ""
        if type == "lower":
            case = string.ascii_lowercase
        if type == "upper":
            case = string.ascii_uppercase
        if type == "digits":
            case = string.digits
        if type == "mix":
            case = string.ascii_letters + string.digits
        else:
            case = string.ascii_letters
        return alpha_num.join(random.choice(case) for i in range(length))

    def get_unique_name(self, char_count=10):
        """ Generates a unique name """
        return self.get_alpha_numeric(char_count, "lower")

    def get_unique_name_list(self, list_size=5, item_length=None):
        """ Get a list of valid names

        :param list_size: Number of names. Default is 5 names in a list
        :param item_length: It should be a list containing number of items
                            equal to the list_size. This determines the length
                            of each item in the list -> [1, 2, 3, 4, 5]
        """
        name_list = []
        for i in range(0, list_size):
            name_list.append(self.get_unique_name(item_length[i]))
        return name_list

    def verify_text_contains(self, actual_text, expected_text):
        """ Verify actual text contains expected text string

        :return: True or False
        """
        self.log.info("Actual text from Application Web UI -> :: "
                      + actual_text)
        self.log.info("Expected text from Application Web UI -> :: "
                      + expected_text)
        if expected_text.lower() in actual_text.lower():
            self.log.info("### VERIFICATION CONTAINS !!!")
            return True
        else:
            self.log.error("### VERIFICATION DOES NOT CONTAIN !!!")
            return False

    def verify_text_match(self, actual_text, expected_text):
        """ Verify expected text matches with actual text

        :return: True or False
        """
        self.log.info("Actual text from Application Web UI -> :: "
                      + actual_text)
        self.log.info("Expected text from Application Web UI -> :: "
                      + expected_text)
        if expected_text.lower() == actual_text.lower():
            self.log.info("### VERIFICATION MATCH !!!")
            return True
        else:
            self.log.error("### VERIFICATION DOES NOT MATCH !!!")
            return False

    def verifyListMatch(self, expected_list, actual_list):
        """ Verify two lists match

        :return: True or False
        """
        return set(expected_list) == set(actual_list)

    def verify_list_contains(self, expected_list, actual_list):
        """ Verify actual list contains elements of expected list

        :return: True or False
        """
        length = len(expected_list)
        for i in range(0, length):
            if expected_list[i] not in actual_list:
                return False
        else:
            return True
