from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class BasePage(object):

  def __init__(self, driver):
    self.driver = driver
    self.timeout = 30

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

  def close_browser(self):
    self.driver.close()
