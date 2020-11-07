import logging

from Locators.cart_page_locators import CartLocators
from Objects.product import Product
from Pages.base_page import BasePage


class CartPage(BasePage):
  def __init__(self, driver):
    super().__init__(driver)
    logging.basicConfig(format='%(asctime)s - %(message)s', level=logging.INFO)

  def click_continue_shopping(self):
    self.click(CartLocators.CONTINUE_SHOPPING_BUTTON)

  def click_remove_product(self, index):
    self.click(CartLocators.BUTTON_REMOVE_FROM_CART(index))

  def get_product_info(self, index):
    name = self.get_text(CartLocators.LABEL_PRODUCT_NAME(index))
    desc = self.get_text(CartLocators.LABEL_PRODUCT_DESC(index))
    price = self.get_text(CartLocators.LABEL_PRODUCT_PRICE(index))
    quantity = self.get_text(CartLocators.LABEL_PRODUCT_QUANTITY(index))
    return Product(name, desc, price, quantity)

  def click_check_out_button(self):
    self.click(CartLocators.CHECK_OUT_BUTTON)
