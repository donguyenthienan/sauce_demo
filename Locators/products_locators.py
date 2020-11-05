from selenium.webdriver.common.by import By


class ProductsLocators(object):
  """A class for products page locators. All products page locators should come here"""
  IMG_BROKEN = (By.XPATH, '//img[contains(@src, "jpgWithGarbageOnItToBreakTheUrl")]')
  _CART_ITEM = "//div[@class='inventory_list']//div[@class='inventory_item']["
  LABEL_SHOPPING_CART_BADGE = (By.CSS_SELECTOR, '.shopping_cart_container .shopping_cart_badge')

  def LABEL_PRODUCT_IMG(index):
    ITEM = "]//div[@class='inventory_item_img']//img"
    return (By.XPATH, (ProductsLocators._CART_ITEM + str(index) + ITEM))

  def LABEL_PRODUCT_NAME(index):
    ITEM = "]//div[@class='inventory_item_name']"
    return (By.XPATH, (ProductsLocators._CART_ITEM + str(index) + ITEM))

  def LABEL_PRODUCT_DESC(index):
    ITEM = "]//div[@class='inventory_item_desc']"
    return (By.XPATH, (ProductsLocators._CART_ITEM + str(index) + ITEM))

  def LABEL_PRODUCT_PRICE(index):
    ITEM = "]//div[@class='inventory_item_price']"
    return (By.XPATH, (ProductsLocators._CART_ITEM + str(index) + ITEM))

  def BUTTON_ADD_TO_CART(index):
    ITEM = "]//button[text()='ADD TO CART']"
    return (By.XPATH, (ProductsLocators._CART_ITEM + str(index) + ITEM))

  def BUTTON_REMOVE_FROM_CART(index):
    ITEM = "]//button[text()='REMOVE']"
    return (By.XPATH, (ProductsLocators._CART_ITEM + str(index) + ITEM))
