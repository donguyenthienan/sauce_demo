import json

from Objects.check_out_info import CheckoutInfo
from Objects.product import Product


class TestData:
  LOGIN_URL = "https://www.saucedemo.com/index.html"
  STANDARD_USER = "standard_user"
  LOCKED_OUT_USER = "locked_out_user"
  PROBLEM_USER = "problem_user"
  PERFORMANCE_GLITCH_USER = "performance_glitch_user"
  PASSWORD = "secret_sauce"
  BROWSER = "chrome"
  FILE = 'TestData/testdata.json'

  def getProducts(self):
    products = []
    with open(TestData.FILE) as json_file:
      data = json.load(json_file)
      for item in data['product']:
        product = Product(item['name'], item['desc'], item['price'])
        products.append(product)
      json_file.close()

    return products

  def get_check_out_info(self):
    with open(TestData.FILE) as json_file:
      data = json.load(json_file)
      item = data['checkout']
      check_out_info = CheckoutInfo(item['firstname'], item['lastname'], item['zipcode'])
      json_file.close()

    return check_out_info
