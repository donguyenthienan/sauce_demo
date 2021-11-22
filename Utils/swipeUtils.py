from appium.webdriver.common.touch_action import TouchAction

from Utils.DriverUtils import DriverUtils


class SwipeUtils:

    def swipeToOpenNotification(self):
        TouchAction(DriverUtils.appiumDriver).press(x=DriverUtils.width / 2, y=0).wait(1000).move_to(x=DriverUtils.width / 2,
                                                                                               y=DriverUtils.height / 2).release().perform()

    def swipeToCloseNotification(self):
        TouchAction(DriverUtils.appiumDriver).press(x=DriverUtils.width / 2, y=DriverUtils.height / 2).wait(1000).move_to(
            x=DriverUtils.width / 2, y=0).release().perform()
