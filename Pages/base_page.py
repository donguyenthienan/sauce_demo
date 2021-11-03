import logging

from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from seleniumpagefactory import PageFactory

from Drivers.Browser import BROWSER
from Utils.DriverUtils import DriverUtils


class BasePage(PageFactory):
  def __init__(self):
    # self.driver = BaseTest.browser.INSTANCE
    self.driver = DriverUtils.driver.INSTANCE
    self.timeout = 30
    self.driver.implicitly_wait(60)



  def navigate_to(self, url):
    self.driver.get(url)

  def click(self, by_locator):
    message = "Click on element with locator '{}'"
    WebDriverWait(self.driver, self.timeout).until(EC.visibility_of_element_located(by_locator)).click()

  def enter_text(self, by_locator, txt):
    element = WebDriverWait(self.driver, self.timeout).until(EC.visibility_of_element_located(by_locator))
    element.clear()
    element.send_keys(txt)

  def get_text(self, by_locator):
    element = WebDriverWait(self.driver, self.timeout).until(EC.visibility_of_element_located(by_locator))
    return element.text

  # def get_web_element(self, *loc):
  #   element = WebDriverWait(self.driver, self.timeout).until(EC.visibility_of_element_located(*loc))
  #   self.highlight_web_element(element)
  #   return element

  def get_elements_size(self, by_locator):
    WebDriverWait(self.driver, self.timeout).until(EC.visibility_of_all_elements_located(by_locator))
    print(by_locator)
    elements = self.driver.find_elements(*by_locator)
    return len(elements)

  def is_visible(self, by_locator):
    element = WebDriverWait(self.driver, self.timeout).until(EC.visibility_of_element_located(by_locator))
    return element.is_displayed()

  def is_exist(self, by_locator):
    elements = WebDriverWait(self.driver, self.timeout).until(EC.presence_of_all_elements_located(by_locator))
    return len(elements)

  # this function checks if the web element whose locator has been passed to it, is enabled or not and returns
  # web element if it is enabled.
  def is_enabled(self, by_locator):
    message = "Check the element with the locator '{}' is enabled or not"
    logging.info(message.format(','.join(by_locator)))

    element = WebDriverWait(self.driver, self.timeout).until(EC.visibility_of_element_located(by_locator))
    return element.is_enabled()

    # this function checks if the web element whose locator has been passed to it, is visible or not and returns
    # true or false depending upon its visibility.

  def is_visible(self, by_locator):
    message = "Check the element with the locator '{}' is visible or not"
    logging.info(message.format(','.join(by_locator)))

    element = WebDriverWait(self.driver, self.timeout).until(EC.visibility_of_element_located(by_locator))
    return element.is_displayed()

  def is_invisible(self, by_locator):
    message = "Check the element with the locator '{}' is visible or not"
    logging.info(message.format(','.join(by_locator)))

    flag = False
    try:
      element = self.driver.find_element(by_locator)
      element.is_displayed()
    except:
      flag = True
      pass

    return flag

  def close_browser(self):
    self.driver.close()
