import unittest

from Objects.account import Account
from Pages.cart_page import CartPage
from Pages.check_out_overview_page import CheckoutOverviewPage
from Pages.check_out_page import CheckoutPage
from Pages.login_page import LoginPage
from Pages.products_page import ProductsPage
from TestCases.base_test import BaseTest
from TestData.TestData import TestData
from Utils.assertion import Assertion


class ProductTestCases(BaseTest):
  def setUp(self):
    super().setUp()

  def tearDown(self):
    super().tearDown()

  def test_product(self):
    login_page = LoginPage(self.driver)
    account = Account(TestData.STANDARD_USER, TestData.PASSWORD)
    login_page.login(account)

    products_page = ProductsPage(self.driver)
    assertion = Assertion()
    products = TestData.getProducts(self)

    for index in [1, 2, 3]:
      products_page.add_product_to_cart(index)

    products_page.click_product_badge()
    cart_page = CartPage(self.driver)
    for index in [1, 2, 3]:
      assertion.compare_products(cart_page.get_product_info(index), products[index - 1])

    cart_page.click_check_out_button()
    check_out_page = CheckoutPage(self.driver)
    check_out_page.enter_to_first_name_textbox('An')
    check_out_page.enter_to_last_name_textbox('Do')
    check_out_page.enter_to_zip_textbox('123')
    check_out_page.click_continue_button()

    check_out_overview_page = CheckoutOverviewPage(self.driver)
    payment_info = check_out_overview_page.get_payment_info()


if __name__ == '__main__':
  # unittest.TestLoader.sortTestMethodsUsing = None
  loader = unittest.TestLoader()
  loader.sortTestMethodsUsing = None
  unittest.main(testLoader=loader, verbosity=2)
