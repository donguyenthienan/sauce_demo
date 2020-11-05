import os
import sys

import HtmlTestRunner

from TestCases.login_test_cases import LoginTestCases

sys.path.append(".")

import unittest

# get all test on login class
login = unittest.TestLoader().loadTestsFromTestCase(LoginTestCases)

# get workspace/project path
dir = os.getcwd()

test_suite = unittest.TestSuite([login])

testRunner = HtmlTestRunner.HTMLTestRunner(output='Reports', verbosity=2, report_name='DemoSauce',
                                           report_title='DemoSauce')
testRunner.run(test_suite)
