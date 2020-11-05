import logging

from Locators.checkout_overview_page_locators import CheckoutOverviewLocators
from Objects.payment_info import PaymentInfo
from Pages.base_page import BasePage


class CheckoutOverviewPage(BasePage):

  def __init__(self, driver):
    super().__init__(driver)
    logging.basicConfig(format='%(asctime)s - %(message)s', level=logging.INFO)

  def get_payment_info(self):
    item_total = self.get_text(CheckoutOverviewLocators.SUMMARY_SUBTOTAL_LABEL)
    tax = self.get_text(CheckoutOverviewLocators.SUMMARY_TAX_LABEL)
    total = self.get_text(CheckoutOverviewLocators.SUMMARY_TOTAL_LABEL)
    return PaymentInfo(item_total, tax, total)

  def click_finish_button(self):
    self.click(CheckoutOverviewLocators.FINISH_BUTTON)
