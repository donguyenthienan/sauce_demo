from Utils.swipeUtils import SwipeUtils
from appiumDemo.Pages.base_page import BasePage


def test_appium1(appiumDriver):
    el = appiumDriver.find_element_by_accessibility_id('Login')
    el.click()


def test_appium2(appiumDriver):
    el = appiumDriver.find_element_by_accessibility_id('Forms')
    el.click()



def test_appium3():
    BasePage().click_menu("Forms")


def test_swipe():
    SwipeUtils().swipeToOpenNotification()
    SwipeUtils().swipeToCloseNotification()
