from pages.courses.register_courses_page import RegisterCoursesPage
from pages.home.navigation_page import NavigationPage
from utilities.checkpoint import CheckPoint
from utilities.read_data import get_csv_data
from ddt import ddt, data, unpack
import unittest
import pytest


@pytest.mark.usefixtures("oneTimeSetUp", "setUp")
@ddt
class RegisterCoursesCSVDataTests(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def objectSetup(self, oneTimeSetUp):
        self.courses = RegisterCoursesPage(self.driver)
        self.cp = CheckPoint(self.driver)
        self.nav = NavigationPage(self.driver)

    def setUp(self):
        self.nav.go_to_main()

    @pytest.mark.run(order=1)
    @data(*get_csv_data("testdata.csv"))
    @unpack
    def test_invalidEnrollment(self, course_name, cc_num, cc_exp, cc_cvv,
                               country, zip):
        self.courses.search_course(course_name)
        self.courses.select_course_to_enroll(course_name)
        self.courses.enroll_course(cc_num, cc_exp, cc_cvv, country, zip)
        result = self.courses.verify_enroll_failed()
        self.cp.mark_final("test_invalidEnrollment", result,
                           "Enrollment failed verification")

