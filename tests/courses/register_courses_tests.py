from pages.courses.register_courses_page import RegisterCoursesPage
from utilities.checkpoint import CheckPoint
import unittest
import pytest


@pytest.mark.usefixtures("oneTimeSetUp", "setUp")
class RegisterCoursesTest(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def classSetup(self):
        self.courses = RegisterCoursesPage(self.driver)
        self.cp = CheckPoint(self.driver)

    @pytest.mark.run(order=1)
    def test_invalidEnrollment(self):
        self.courses.search_course("JavaScript")
        self.courses.select_course_to_enroll("JavaScript for beginners")
        self.courses.enroll_course("1234 5678 9012 3456", "1220", "444",
                                   "Brazil", "18000")
        result = self.courses.verify_enroll_failed()
        self.cp.mark_final("test_invalidEnrollment", result,
                           "Enrollment failed verification")
