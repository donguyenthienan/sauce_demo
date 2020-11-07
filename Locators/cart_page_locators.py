from selenium.webdriver.common.by import By


class CartLocators:
  CONTINUE_SHOPPING_BUTTON = (By.XPATH, '//a[text()="Continue Shopping"]')
  CHECK_OUT_BUTTON = (By.XPATH, '//a[text()="CHECKOUT"]')
  PREFIX = '//div[@class="cart_list"]//div[@class="cart_item"]['

  def LABEL_PRODUCT_NAME(index):
    ITEM = ']//div[@class="inventory_item_name"]'
    return (By.XPATH, (CartLocators.PREFIX + str(index) + ITEM))

  def LABEL_PRODUCT_DESC(index):
    ITEM = ']//div[@class="inventory_item_desc"]'
    return (By.XPATH, (CartLocators.PREFIX + str(index) + ITEM))

  def LABEL_PRODUCT_PRICE(index):
    ITEM = ']//div[@class="inventory_item_price"]'
    return (By.XPATH, (CartLocators.PREFIX + str(index) + ITEM))

  def LABEL_PRODUCT_QUANTITY(index):
    ITEM = ']/div[@class="cart_quantity"]'
    return (By.XPATH, (CartLocators.PREFIX + str(index) + ITEM))

  def BUTTON_REMOVE_FROM_CART(index):
    ITEM = ']//button[text()="REMOVE"]'
    return (By.XPATH, (CartLocators.PREFIX + str(index) + ITEM))
