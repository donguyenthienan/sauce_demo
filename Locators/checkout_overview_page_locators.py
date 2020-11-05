from selenium.webdriver.common.by import By


class CheckoutOverviewLocators(object):
  """A class for products page locators. All products page locators should come here"""
  SUMMARY_SUBTOTAL_LABEL = (By.CLASS_NAME, 'summary_subtotal_label')
  SUMMARY_TAX_LABEL = (By.CLASS_NAME, 'summary_tax_label')
  SUMMARY_TOTAL_LABEL = (By.CLASS_NAME, 'summary_total_label')
  FINISH_BUTTON = (By.XPATH, '//a[text()="FINISH"]')
