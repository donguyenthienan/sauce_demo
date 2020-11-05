from selenium.webdriver.common.by import By


class CheckoutLocators(object):
  """A class for products page locators. All products page locators should come here"""
  FIRST_NAME_TEXTBOX = (By.ID, 'first-name')
  LAST_NAME_TEXTBOX = (By.ID, 'last-name')
  POSTAL_CODE_TEXTBOX = (By.ID, 'postal-code')
  CONTINUE_BUTTON = (By.CSS_SELECTOR, 'input[value=CONTINUE]')
  CANCEL_BUTTON = (By.XPATH, '//a[text()="CANCEL"]')
