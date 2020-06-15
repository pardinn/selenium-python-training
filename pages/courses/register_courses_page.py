import logging
import utilities.custom_logger as cl
from base.base_page import BasePage


class RegisterCoursesPage(BasePage):
    log = cl.custom_logger(logging.DEBUG)

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # locators
    _search_box = "search-courses"  # id
    _search_button = "search-course-button"  # id
    _course = "//div[contains(@class,'course-listing-title') and contains(" \
              "text(), '{0}')]"  # xpath
    _all_courses = "course-listing-title"  # class
    _enroll_button = "enroll-button-top"  # id
    _cc_num = "cardnumber"  # name
    _cc_exp = "exp-date"  # name
    _cc_cvv = "cvc"
    _cc_country = "country_code_credit_card-cc"  # id
    _cc_zip = "postal"  # name
    _terms_checkbox = "agreed_to_terms_checkbox"  # id
    _submit_enroll = "confirm-purchase"  # id
    _enroll_error_message = "//div[@class='payment-error-box']//span"  # xpath

    def enter_course_name(self, name):
        self.send_keys(name, self._search_box)

    def click_search_button(self):
        self.click_element(self._search_button)

    def select_course_to_enroll(self, full_course_name):
        self.click_element(self._course.format(full_course_name), "xpath")

    def click_on_enroll_button(self):
        self.click_element(self._enroll_button)

    def enter_card_number(self, cc_num):
        self.wait_for_element("iframe", "tag")
        # self.switch_to_frame("__privateStripeFrame16")
        self.switch_to_dynamic_frame(self._cc_num, "name")
        self.send_keys_with_delay(cc_num, self._cc_num, "name")
        self.switch_to_default_content()

    def enter_expiration_date(self, exp_date):
        # self.switch_to_frame("__privateStripeFrame17")
        self.switch_to_dynamic_frame(self._cc_exp, "name")
        self.send_keys_with_delay(exp_date, self._cc_exp, "name")
        self.switch_to_default_content()

    def enter_cvc_code(self, cvv):
        # self.switch_to_frame("__privateStripeFrame18")
        self.switch_to_dynamic_frame(self._cc_cvv, "name")
        self.send_keys(cvv, self._cc_cvv, "name")
        self.switch_to_default_content()

    def select_country(self, country):
        self.select_by_visible_text(country, self._cc_country)

    def enter_postal_code(self, postal_code):
        # self.switch_to_frame("__privateStripeFrame19")
        self.switch_to_dynamic_frame(self._cc_zip, "name")
        self.send_keys(postal_code, self._cc_zip, "name")
        self.switch_to_default_content()

    def click_agree_to_terms_checkbox(self):
        self.click_element(self._terms_checkbox)

    def click_enroll_submit_button(self):
        self.click_element(self._submit_enroll, "xpath")

    def search_course(self, course_name):
        self.enter_course_name(course_name)
        self.click_search_button()

    def enter_credit_card_information(self, num, exp, cvv, country, zip):
        self.enter_card_number(num)
        self.enter_expiration_date(exp)
        self.enter_cvc_code(cvv)
        self.select_country(country)
        self.enter_postal_code(zip)

    def enroll_course(self, num="", exp="", cvv="", country="", zip_code=""):
        self.click_on_enroll_button()
        self.web_scroll("down")
        self.enter_credit_card_information(num, exp, cvv, country, zip_code)
        # self.click_agree_to_terms_checkbox()

    def verify_enroll_failed(self):
        return not self.is_enabled(self._submit_enroll, info="Enroll Button")
