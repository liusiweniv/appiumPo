from hamcrest import assert_that, close_to
from appium import  webdriver

def test_a():
    desired_caps = {}
    desired_caps['platformName'] = 'Android'
    desired_caps['deviceName'] = '127.0.0.1:5555'
    desired_caps['noReset'] = 'true'
    desired_caps['app'] = '/Users/zhangniuniu/Downloads/appiumWap/app/maodou.apk'
    desired_caps['appPackage'] = 'com.guazi.newcar'
    desired_caps['appActivity'] = 'com.guazi.newcar.modules.splash.SplashActivity'

    # 设置中文输入
    desired_caps['unicodeKeyBoard'] = 'true'
    desired_caps['resetKeyBoard'] = 'true'
    # 在哪个页面，就在哪个页面操作
    desired_caps['dontStopAppOnreset'] = 'true'
    driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desired_caps)
    driver.implicitly_wait(5)
    driver.quit()
    driver.find_element_by_android_uiautomator('new Uiselector().resourceId()')

def test_assert():
    print('11')
    assert_that(0, close_to(10, 2))

