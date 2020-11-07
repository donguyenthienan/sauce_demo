import unittest

from Objects.account import Account
from Objects.payment_info import PaymentInfo
from Pages.cart_page import CartPage
from Pages.check_out_overview_page import CheckoutOverviewPage
from Pages.check_out_page import CheckoutPage
from Pages.login_page import LoginPage
from Pages.products_page import ProductsPage
from TestCases.base_test import BaseTest
from TestData.TestData import TestData
from Utils import utils
from Utils.assertion import Assertion


class ProductTestCases2(BaseTest):
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
    check_out_page.input_check_out_data(TestData.get_check_out_info(self))
    check_out_page.click_continue_button()

    check_out_overview_page = CheckoutOverviewPage(self.driver)
    actual_payment_info = check_out_overview_page.get_payment_info()
    actual_item_total = utils.convert_string_to_float(actual_payment_info.item_total)
    actual_total = utils.convert_string_to_float(actual_payment_info.total)
    actual_tax = utils.convert_string_to_float(actual_payment_info.tax)
    tax_rate = 0.08
    expected_tax = float("{:.2f}".format(actual_item_total * tax_rate))
    expected_total = float("{:.2f}".format(expected_tax + actual_item_total))
    assertion.assertEqual(actual_total, expected_total)
    assertion.assertEqual(actual_tax, expected_tax)


if __name__ == '__main__':
  # unittest.TestLoader.sortTestMethodsUsing = None
  loader = unittest.TestLoader()
  loader.sortTestMethodsUsing = None
  unittest.main(testLoader=loader, verbosity=2)
