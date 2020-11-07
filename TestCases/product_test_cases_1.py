import unittest

from Objects.account import Account
from Objects.product import Product
from Pages.login_page import LoginPage
from Pages.products_page import ProductsPage
from TestCases.base_test import BaseTest
from TestData.TestData import TestData
from Utils.assertion import Assertion


class ProductTestCases1(BaseTest):
  def setUp(self):
    super().setUp()

  def tearDown(self):
    super().tearDown()

  # @unittest.skip('Thich')
  def test_product(self):
    expected_product = Product('Sauce Labs Bolt T-Shirt',
                               'Get your testing superhero on with the Sauce Labs bolt T-shirt. From American Apparel, 100% ringspun combed cotton, heather gray with red bolt.',
                               '$15.99')
    login_page = LoginPage(self.driver)
    account = Account(TestData.STANDARD_USER, TestData.PASSWORD)
    login_page.login(account)
    product_page = ProductsPage(self.driver)
    product_page.add_product_to_cart(1)
    self.assertTrue(product_page.is_remove_button_exist(1))
    self.assertEqual(product_page.get_cart_number(), 1)
    product_page.remove_product_from_cart(1)
    self.assertTrue(product_page.does_add_button_exist(1))
    self.assertEqual(product_page.get_product_info(1).__init__(), expected_product.__init__())

  def test_products_display_correctly(self):
    products_page = ProductsPage(self.driver)

    products = TestData.getProducts(self)

    for index, expected_product in enumerate(products, start=1):
      '''Add & remove all products'''
      products_page.add_product_to_cart(index)
      self.assertTrue(products_page.does_remove_button_exist(index))
      self.assertEqual(1, products_page.get_product_badge())

      products_page.remove_product_from_cart(index)
      self.assertTrue(products_page.does_add_button_exist(index))
      self.assertTrue(products_page.is_product_badge_invisible())

      actual_product = products_page.get_product_info(index)
      assertion = Assertion()
      assertion.compare_products(actual_product, expected_product)


if __name__ == '__main__':
  # unittest.TestLoader.sortTestMethodsUsing = None
  loader = unittest.TestLoader()
  loader.sortTestMethodsUsing = None
  unittest.main(testLoader=loader, verbosity=2)
