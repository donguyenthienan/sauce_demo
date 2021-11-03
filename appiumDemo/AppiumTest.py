from appium import webdriver

desired_caps = dict(
    platformName='Android',
    platformVersion='5.0',
    automationName='uiautomator2',
    deviceName='Android Emulator',
    udid='emulator-5554',
    appPackage='com.wdiodemoapp',
    appActivity='com.wdiodemoapp.SplashActivity'
    #app=PATH('../../../apps/selendroid-test-app.apk')
)
driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
driver.implicitly_wait(5)
el = driver.find_element_by_accessibility_id('Login')
el.click()

