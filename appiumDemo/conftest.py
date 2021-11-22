import pytest
from appium import webdriver
from appium.webdriver.appium_service import AppiumService

from Utils.DriverUtils import DriverUtils


@pytest.fixture(autouse=True, scope="session")
def appiumDriver(setDown):
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
    DriverUtils.width = DriverUtils.appiumDriver.get_window_size().get('width')
    DriverUtils.height = DriverUtils.appiumDriver.get_window_size().get('height')
    return DriverUtils.appiumDriver

@pytest.fixture(scope="session")
def setDown():
    appium_service = AppiumService()
    appium_service.start(hihi="")
    yield
    DriverUtils.appiumDriver.quit()
    appium_service.stop()