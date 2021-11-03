import pytest

from Drivers.Browser import BROWSER
from TestData.TestData import TestData
from Utils.DriverUtils import DriverUtils

@pytest.fixture(autouse=True)
def setUp():
    # BaseTest.browser = BROWSER()
    # self.driver = BaseTest.browser.INSTANCE
    DriverUtils.driver = BROWSER()
    driver = DriverUtils.driver.INSTANCE
    driver.maximize_window()
    driver.get(TestData.LOGIN_URL)
    yield
    try:
        driver.close()
        driver.quit()
    except Exception as mess:
        print("message %s" % str(mess))
        pass

@pytest.fixture
def driver():
    return DriverUtils.driver.INSTANCE
