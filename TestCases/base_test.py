import sys
import unittest

from Drivers.Browser import BROWSER
from TestData.TestData import TestData
from Utils.DriverUtils import DriverUtils

sys.path.append(".")


class BaseTest(unittest.TestCase):
  # browser = None
  def setUp(self):
    # BaseTest.browser = BROWSER()
    # self.driver = BaseTest.browser.INSTANCE
    DriverUtils.driver = BROWSER()
    self.driver = DriverUtils.driver.INSTANCE
    self.driver.maximize_window()
    self.driver.get(TestData.LOGIN_URL)

  def tearDown(self):
    try:
      self.driver.close()
      self.driver.quit()
    except Exception as mess:
      print("message %s" % str(mess))
      pass

  # def getBROWSER(self):
  #   return self.browser
  #
  # browser = property(getBROWSER)