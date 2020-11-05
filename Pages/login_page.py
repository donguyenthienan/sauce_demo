import sys

from Locators.login_page_locators import LoginPageLocators
from Pages.home_page import HomePage

sys.path.append(".")


class LoginPage(HomePage):

  def __init__(self, driver):
    super().__init__(driver)

  def login(self, account):
    self.enter_text(LoginPageLocators.INPUT_USERNAME, account.username)
    self.enter_text(LoginPageLocators.INPUT_PASSWORD, account.password)
    self.click(LoginPageLocators.BTN_LOGIN)
