import logging

from Locators.checkout_page_locators import CheckoutLocators
from Pages.base_page import BasePage


class CheckoutPage(BasePage):

  def __init__(self, driver):
    super().__init__(driver)
    logging.basicConfig(format='%(asctime)s - %(message)s', level=logging.INFO)

  def input_check_out_data(self, check_out_info):
    self.enter_text(CheckoutLocators.FIRST_NAME_TEXTBOX, check_out_info.first_name)
    self.enter_text(CheckoutLocators.LAST_NAME_TEXTBOX, check_out_info.last_name)
    self.enter_text(CheckoutLocators.POSTAL_CODE_TEXTBOX, check_out_info.zip_code)

  def click_continue_button(self):
    self.click(CheckoutLocators.CONTINUE_BUTTON)

  def click_cancel_button(self):
    self.click(CheckoutLocators.CANCEL_BUTTON)
