import os
from TestData.TestData import TestData
from selenium import webdriver
import sys


class BROWSER(object):

    def __init__(self):
        self.driver = None

    def getInstance(self):
        if (self.driver == None):
            self.setInstance()
        return self.driver

    def setInstance(self):
        self.driver = self.startBrowser(str(self.get_browser()))

    # driver = getInstance()
    # _driver = None
    INSTANCE = property(getInstance, setInstance)

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
                return webdriver.Chrome(executable_path=sys.path[0] + '\\Drivers\\chromedriver.exe')
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
