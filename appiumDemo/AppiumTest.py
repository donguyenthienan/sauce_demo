def test_appium1(driver):
    el = driver.find_element_by_accessibility_id('Login')
    el.click()


def test_appium2(driver):
    el = driver.find_element_by_accessibility_id('Forms')
    el.click()

