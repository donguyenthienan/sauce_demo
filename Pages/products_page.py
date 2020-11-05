import logging

from Locators.products_locators import ProductsLocators
from Objects.product import Product
from Pages.base_page import BasePage


class ProductsPage(BasePage):

  def __init__(self, driver):
    super().__init__(driver)
    logging.basicConfig(format='%(asctime)s - %(message)s', level=logging.INFO)

  def get_broken_image(self):
    return self.get_elements_size(ProductsLocators.IMG_BROKEN)

  def add_product_to_cart(self, index):
    self.click(ProductsLocators.BUTTON_ADD_TO_CART(index))

  def remove_product_from_cart(self, index):
    self.click(ProductsLocators.BUTTON_REMOVE_FROM_CART(index))

  def get_product_info(self, index):
    name = self.get_text(ProductsLocators.LABEL_PRODUCT_NAME(index))
    desc = self.get_text(ProductsLocators.LABEL_PRODUCT_DESC(index))
    price = self.get_text(ProductsLocators.LABEL_PRODUCT_PRICE(index))
    return Product(name, desc, price)

  def is_remove_button_exist(self, index):
    return self.is_visible(ProductsLocators.BUTTON_REMOVE_FROM_CART(index))

  def does_add_button_exist(self, index):
    return self.is_visible(ProductsLocators.BUTTON_ADD_TO_CART(index))

  def get_cart_number(self):
    total = 0
    try:
      total = self.get_text(ProductsLocators.LABEL_SHOPPING_CART_BADGE)
    except Exception as identifier:
      pass
    return int(total)

  def does_remove_button_exist(self, index):
    return self.is_visible(ProductsLocators.BUTTON_REMOVE_FROM_CART(index))

  def get_product_badge(self):
    total = 0

    try:
      total = self.get_text(ProductsLocators.LABEL_SHOPPING_CART_BADGE)
    except:
      pass
    return int(total)

  def is_product_badge_invisible(self):
    return self.is_invisible(ProductsLocators.LABEL_SHOPPING_CART_BADGE)

  def click_product_badge(self):
    return self.click(ProductsLocators.LABEL_SHOPPING_CART_BADGE)
