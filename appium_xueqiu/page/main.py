from appium.webdriver.common.mobileby import MobileBy

from appium_xueqiu.page.base_page import BasePage
from appium_xueqiu.page.market import Market
import  yaml

class Main(BasePage):
    def goto_market(self):
        #click进入行情页
        # self.find(MobileBy.XPATH, '//*[@text="行情"]').click()
        self.set_implicitly_time(10)
        self.steps('../page/main.yml')
        self.set_implicitly_time(3)
        return Market(self._driver)

