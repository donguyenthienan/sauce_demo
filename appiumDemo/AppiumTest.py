import allure
from _pytest.logging import caplog

from Utils.swipeUtils import SwipeUtils
from appiumDemo.Pages.base_page import BasePage


@allure.step
def passing_step():
    pass


@allure.severity(allure.severity_level.NORMAL)
def test_appium1():
    passing_step()
    caplog
    BasePage().click_menu("Login")


@allure.severity(allure.severity_level.MINOR)
def test_appium2():
    BasePage().click_menu("Forms")


@allure.severity(allure.severity_level.MINOR)
def test_appium3():
    BasePage().click_menu("Forms")


@allure.severity(allure.severity_level.MINOR)
def test_swipe():
    SwipeUtils().swipeToOpenNotification()
    SwipeUtils().swipeToCloseNotification()
