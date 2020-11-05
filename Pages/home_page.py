from Locators.home_page_locators import HomePageLocators
from Pages.base_page import BasePage


class HomePage(BasePage):
  def __init__(self, driver):
    super().__init__(driver)

  def go_to_shopping_cart_page(self):
    self.click(HomePageLocators.SHOPPING_CART_ITEM)
