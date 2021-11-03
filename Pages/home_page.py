from selenium.webdriver.common.by import By

from Locators.home_page_locators import HomePageLocators
from Pages.base_page import BasePage


class HomePage(BasePage):
  def __init__(self):
    super().__init__()

    # define locators dictionary where key name will became WebElement using PageFactory
  locators = {
      "itmShoppingCart": ('ID', 'shopping_cart_container'),
   }

  def go_to_shopping_cart_page(self):
    self.itmShoppingCart.click()
