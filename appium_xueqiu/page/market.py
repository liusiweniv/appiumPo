from appium.webdriver.common.mobileby import MobileBy

from appium_xueqiu.page.base_page import BasePage
from appium_xueqiu.page.search import Search


class Market(BasePage):
    def goto_search(self):
        #点击搜索
        self.find(MobileBy.ID, 'com.xueqiu.android:id/action_search').click()
        return Search(self._driver)