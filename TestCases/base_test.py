import os
import sys
import unittest

from selenium import webdriver

from TestData.TestData import TestData

sys.path.append(".")


class BaseTest(unittest.TestCase):

  def setUp(self):
    browser = self.get_browser()
    self.driver = self.startBrowser(browser)
    self.driver.maximize_window()
    self.driver.get(TestData.LOGIN_URL)

  def tearDown(self):
    try:
      self.driver.close()
      self.driver.quit()
    except Exception as mess:
      print("message %s" % str(mess))
      pass

  def startBrowser(self, name="chrome"):
    """
    browsers，"firefox"、"chrome"、"ie"、"phantomjs"
    """
    try:
      if name.lower() == "firefox" or name.lower() == "ff":
        print("start browser name :Firefox")
        # return webdriver.Firefox(executable_path='')
        return webdriver.Firefox()
      elif name.lower() == "chrome":
        print("start browser name :Chrome")
        return webdriver.Chrome(executable_path=r'D:\sauce_demo\Drivers\chromedriver.exe')
      elif name.lower() == "edge":
        print("start browser name :Edge")
        return webdriver.MicrosoftEdge()
      elif name.lower() == "phantomjs":
        print("start browser name :phantomjs")
        return webdriver.PhantomJS()
      else:
        print("Not found this browser,You can use ‘firefox‘, ‘chrome‘, ‘ie‘ or ‘phantomjs‘")
    except Exception as msg:
      print("message: %s" % str(msg))

  def get_browser(self):
    try:
      return os.environ['BROWSER']
    except KeyError:
      return TestData.BROWSER
