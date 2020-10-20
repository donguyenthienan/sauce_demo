from Locators.login_page_locators import LoginPageLocators
from Pages.base_page import BasePage
import sys

sys.path.append(".")


class LoginPage(BasePage):

  def __init__(self, driver):
    super().__init__(driver)
    self.navigate_to("https://www.saucedemo.com/index.html")

  def login(self, account):
    self.enter_text(LoginPageLocators.INPUT_USERNAME, account.username)
    self.enter_text(LoginPageLocators.INPUT_PASSWORD, account.password)
    self.click(LoginPageLocators.BTN_LOGIN)
