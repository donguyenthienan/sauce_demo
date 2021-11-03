import sys

from Locators.login_page_locators import LoginPageLocators
from Pages.home_page import HomePage

sys.path.append(".")


class LoginPage(HomePage):

  def __init__(self):
    super().__init__()

  locators = {
    "inptUserName": ('ID', 'user-name'),
    "inptPassword": ('ID', 'password'),
    "btnLogin": ('ID', 'login-button')
  }

  def login(self, account):
    self.inptUserName.set_text(account.username)
    self.inptPassword.set_text(account.password)
    self.btnLogin.click_button()
    # self.enter_text(LoginPageLocators.INPUT_USERNAME, account.username)
    # self.enter_text(LoginPageLocators.INPUT_PASSWORD, account.password)
    # self.click(LoginPageLocators.BTN_LOGIN)
