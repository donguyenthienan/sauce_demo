from seleniumpagefactory import PageFactory

from Utils.DriverUtils import DriverUtils


class BasePage(PageFactory):
    def __init__(self):
        # self.driver = BaseTest.browser.INSTANCE
        self.driver = DriverUtils.appiumDriver
        self.timeout = 30
        self.driver.implicitly_wait(60)

        # define locators dictionary where key name will became WebElement using PageFactory

    locators = {
        "formsMenu": ('xpath', '//android.widget.Button[@content-desc="Forms"]'),
    }

    def click_menu(self, menu):
        if(menu == 'Forms'):
            self.formsMenu.click()
        else:
            self.driver.find_element_by_accessibility_id(menu).click()