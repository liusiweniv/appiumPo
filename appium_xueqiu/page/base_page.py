import inspect
import json
import logging

import yaml
from appium.webdriver import WebElement
from appium.webdriver.webdriver import WebDriver
from selenium.webdriver.common.by import By

from appium_xueqiu.page.wrapper import handle_black


class BasePage:
    # 弹框 处理的定位列表
    logging.basicConfig(level=logging.INFO)
    _black_list = [
        (By.XPATH, "//*[@text='确认']"),
        (By.XPATH, "//*[@text='下次再说']"),
        (By.XPATH, "//*[@text='确定']"),
    ]
    _max_num = 3
    _error_num = 0
    _params = {}

    def __init__(self, driver: WebDriver = None):
        self._driver = driver


    def set_implicitly_time(self, time):
        self._driver.implicitly_wait(time)


    def finds(self, locator, value: str = None):
        elements: list
        if isinstance(locator, tuple):
            elements = self._driver.find_elements(*locator)
        else:
            elements = self._driver.find_elements(locator, value)
        return elements

    @handle_black
    def find(self, locator, value: str = None):
        logging.info(locator)
        logging.info(value)
        element: WebElement
        if isinstance(locator, tuple):
            element = self._driver.find_element(*locator)
        else:
            element = self._driver.find_element(locator,value)
        # 找到之前 _error_num 归0
        self._error_num = 0
        # 隐式等待回复原来的等待，
        self._driver.implicitly_wait(10)
        return element

    @handle_black
    def find_and_get_text(self, locator, value: str = None):
        element: WebElement
        # try:
        #     element_text = self._driver.find_element(*locator).text if isinstance(locator,
        #                                                                           tuple) else self._driver.find_element(
        #         locator, value).text
        #     # if isinstance(locator, tuple):
        #     #     element =  self._driver.find_element(*locator)
        #     # else:
        #     #     element = self._driver.find_element(locator,value)
        #     # 找到之前 _error_num 归0
        #     self._error_num = 0
        #     # 隐式等待回复原来的等待，
        #     self._driver.implicitly_wait(10)
        #     return element_text
        # except Exception as e:
        #     # 出现异常， 将隐式等待设置小一点，快速的处理弹框
        #     self._driver.implicitly_wait(1)
        #     # 判断异常处理次数
        #     if self._error_num > self._max_num:
        #         raise e
        #     self._error_num += 1
        #     # 处理黑名单里面的弹框
        #     for ele in self._black_list:
        #         elelist = self._driver.find_elements(*ele)
        #         if len(elelist) > 0:
        #             elelist[0].click()
        #             # 处理完弹框，再将去查找目标元素
        #             return self.find_and_get_text(locator, value)
        #
        #     raise e


        if isinstance(locator, tuple):
            element_text =  self._driver.find_element(*locator).text
        else:
            element_text = self._driver.find_element(locator, value).text
        return element_text


    def steps(self, path):
        with open(path, encoding='utf-8') as f:
            #拿到第一个调用它的，第0个是它自己
            name = inspect.stack()[1].function
            steps = yaml.safe_load(f)[name]

        raw = json.dumps(steps)
        for key, value in self._params.items():
            #在f 转义中，两个{{}}代表一个大括号
            # raw.replace(f'${{{key}}}', value)
            raw = raw.replace('${'+key+'}', value)

        steps = json.loads(raw)

        for step in steps:
            if 'action' in step.keys():
                action = step['action']
                if action == 'click':
                   self.find(step['by'], step['locator']).click()
                if action == 'send':
                   self.find(step['by'], step['locator']).send_keys(step['value'])
                if 'len > 0' == action:
                    elems = self.finds(step['by'], step['locator'])
                    return len(elems) > 0



