from selenium.webdriver.common.by import By


def handle_black(func):
    def wrapper(*args, **kwargs):
        # 弹框 处理的定位列表
        _black_list = [
            (By.XPATH, "//*[@text='确认']"),
            (By.XPATH, "//*[@text='下次再说']"),
            (By.XPATH, "//*[@text='确定']"),
        ]
        _max_num = 3
        _error_num = 0
        from appium_xueqiu.page.base_page import BasePage
        instance : BasePage = args[0]
        try:
            element = func(*args, **kwargs)
            _error_num=0
            instance._driver.implicitly_wait(1)
            return element
        except Exception as e:
            # 判断异常处理次数
            if _error_num > _max_num:
                raise e
            _error_num += 1
            # 处理黑名单里面的弹框
            for ele in _black_list:
                elelist = instance._driver.find_elements(*ele)
                if len(elelist) > 0:
                    elelist[0].click()
                    # 处理完弹框，再将去查找目标元素
                    return wrapper(*args, **kwargs)
            raise e

    return  wrapper





