from selenium.webdriver.common.by import By


class LoginPageLocators(object):
  INPUT_USERNAME = (By.ID, 'user-name')
  INPUT_PASSWORD = (By.ID, 'password')
  BTN_LOGIN = (By.ID, 'login-button')
