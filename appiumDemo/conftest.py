import pytest
from appium import webdriver

from Utils.DriverUtils import DriverUtils


@pytest.fixture
def driver():
    if (DriverUtils.appiumDriver != None):
        return DriverUtils.appiumDriver
    desired_caps = dict(
        platformName='Android',
        platformVersion='5.0',
        automationName='uiautomator2',
        deviceName='Android Emulator',
        udid='emulator-5554',
        appPackage='com.wdiodemoapp',
        appActivity='com.wdiodemoapp.MainActivity'
        # app=PATH('../../../apps/selendroid-test-app.apk')
    )
    driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
    driver.implicitly_wait(5)
    DriverUtils.appiumDriver = driver
    return DriverUtils.appiumDriver

@pytest.fixture(autouse=True, scope="session")
def setDown():
    yield
    DriverUtils.appiumDriver.quit()