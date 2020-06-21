import unittest
from tests.home.test_login import TestLogin
from tests.courses.test_register_courses_csv_data import \
    TestRegisterCoursesCSVData

# Get all tests from the test classes
tc1 = unittest.TestLoader().loadTestsFromTestCase(TestLogin)
tc2 = unittest.TestLoader().loadTestsFromTestCase(TestRegisterCoursesCSVData)

# Create a test suite combining all test classes
smoke_test = unittest.TestSuite([tc1, tc2])

unittest.TextTestRunner(verbosity=2).run(smoke_test)
