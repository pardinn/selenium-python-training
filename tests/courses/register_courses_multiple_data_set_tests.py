from pages.courses.register_courses_page import RegisterCoursesPage
from utilities.checkpoint import CheckPoint
from ddt import ddt, data, unpack
import unittest
import pytest


@pytest.mark.usefixtures("oneTimeSetUp", "setUp")
@ddt
class RegisterCoursesMultipleDataSetTests(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def classSetup(self, oneTimeSetUp):
        self.courses = RegisterCoursesPage(self.driver)
        self.cp = CheckPoint(self.driver)

    @pytest.mark.run(order=1)
    @data(("JavaScript for beginners", "1234 5678 9012 3456", "1220", "444",
           "Brazil", "18000"),
          ("Learn Python 3 from scratch", "6541 8025 4098 5146", "1225", "444",
           "Brazil", "18000"))
    @unpack
    def test_invalidEnrollment(self, course_name, cc_num, cc_exp, cc_cvv,
                               country, zip):
        self.courses.search_course(course_name)
        self.courses.select_course_to_enroll(course_name)
        self.courses.enroll_course(cc_num, cc_exp, cc_cvv, country, zip)
        result = self.courses.verify_enroll_failed()
        self.cp.mark_final("test_invalidEnrollment", result,
                           "Enrollment failed verification")
        self.driver.find_element_by_xpath(
            "//a[@class='navbar-brand header-logo']").click()
