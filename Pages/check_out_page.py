import logging

from Locators.checkout_page_locators import CheckoutLocators
from Pages.base_page import BasePage


class CheckoutPage(BasePage):

  def __init__(self, driver):
    super().__init__(driver)
    logging.basicConfig(format='%(asctime)s - %(message)s', level=logging.INFO)

  def enter_to_first_name_textbox(self, text):
    self.enter_text(CheckoutLocators.FIRST_NAME_TEXTBOX, text)

  def enter_to_last_name_textbox(self, text):
    self.enter_text(CheckoutLocators.LAST_NAME_TEXTBOX, text)

  def enter_to_zip_textbox(self, text):
    self.enter_text(CheckoutLocators.POSTAL_CODE_TEXTBOX, text)

  def click_continue_button(self):
    self.click(CheckoutLocators.CONTINUE_BUTTON)

  def click_cancel_button(self):
    self.click(CheckoutLocators.CANCEL_BUTTON)
