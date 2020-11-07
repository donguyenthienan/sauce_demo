import os
import sys

import HtmlTestRunner

from TestCases.login_test_cases import LoginTestCases
from TestCases.product_test_cases_1 import ProductTestCases1
from TestCases.product_test_cases_2 import ProductTestCases2

sys.path.append(".")

import unittest

# get all test on login class
login = unittest.TestLoader().loadTestsFromTestCase(LoginTestCases)
product1 = unittest.TestLoader().loadTestsFromTestCase(ProductTestCases1)
product2 = unittest.TestLoader().loadTestsFromTestCase(ProductTestCases2)

# get workspace/project path
proj_dir = os.getcwd()

test_suite = unittest.TestSuite([login, product1, product2])

testRunner = HtmlTestRunner.HTMLTestRunner(output='Reports', verbosity=2, report_name='DemoSauce',
                                           report_title='DemoSauce')
testRunner.run(test_suite)
