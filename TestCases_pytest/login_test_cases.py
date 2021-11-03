from Objects.account import Account
from Pages.login_page import LoginPage
from TestData.TestData import TestData



def test_login_with_standard_user(driver):
  timeout = 5
  login_page = LoginPage()
  account = Account(TestData.STANDARD_USER, TestData.PASSWORD)
  login_page.login(account)
  assert driver.current_url == 'https://www.saucedemo.com/inventory.html', 'Làm lại đi'

  # def test_login_with_locked_out_user(self):
  #   self.login_page = LoginPage()
  #   account = Account(TestData.LOCKED_OUT_USER, TestData.PASSWORD)
  #   self.login_page.login(account)
  #   message = self.driver.find_element_by_xpath(LoginPageLocators.ERROR_MESSAGE).text
  #   print(message)
  #   self.assertIn(self.driver.current_url, 'https://www.saucedemo.com/index.html', 'Làm lại đi')
  #   self.assertIn('Epic sadface: Sorry, this user has been locked out.', message, 'Làm lại đi')
  #
  # def test_login_with_problem_user(self):
  #   login_page = LoginPage()
  #   account = Account(TestData.PROBLEM_USER, TestData.PASSWORD)
  #   login_page.login(account)
  #   self.assertIn(self.driver.current_url, 'https://www.saucedemo.com/inventory.html', 'Làm lại đi')
  #   products_page = ProductsPage(self.driver)
  #   num = products_page.get_broken_image()
  #   print(num)
  #   self.assertEqual(0, num, 'Bug--------------------------------')
  #   print(products_page.get_product_info(1))
  #   print(products_page.get_product_info(2))
  #   print(products_page.get_product_info(3))
  #   print(products_page.get_product_info(4))
  #   print(products_page.get_product_info(5))
  #   print(products_page.get_product_info(6))
  #   product_list = []
  #   for i in range(1, 7):
  #     product_list.append(products_page.get_product_info(i).__str__())
  #   print(product_list)
  #
  # def test_login_with_performance_glitch_user(self):
  #   self.login_page = LoginPage()
  #   account = Account(TestData.PERFORMANCE_GLITCH_USER, TestData.PASSWORD)
  #   self.login_page.login(account)
  #   self.assertIn(self.driver.current_url, 'https://www.saucedemo.com/inventory.html', 'Làm lại đi')


# if __name__ == '__main__':
#   # unittest.TestLoader.sortTestMethodsUsing = None
#   loader = unittest.TestLoader()
#   loader.sortTestMethodsUsing = None
#   unittest.main(testLoader=loader, verbosity=2)
