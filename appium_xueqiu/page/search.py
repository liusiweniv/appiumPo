from appium.webdriver.common.mobileby import MobileBy

from appium_xueqiu.page.base_page import BasePage
import  yaml

class Search(BasePage):
    #点击搜索框，输入阿里巴巴，点击搜索
    def search(self, name):
        self._params['name'] = name
        self.steps('../page/search.yml')

    def add(self, name):
        self._params['name'] = name
        self.steps('../page/search.yml')

    def is_choose(self, name):
        self._params['name'] = name
        return self.steps('../page/search.yml')

    def reset(self, name):
        self._params['name'] = name
        return self.steps('../page/search.yml')




