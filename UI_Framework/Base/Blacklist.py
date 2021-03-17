from appium.webdriver.common.mobileby import MobileBy

from UI_Framework.Base import logger


def Black_list(fun):
    def run(*args, **kwargs):
        black_list = ["//*[@resource-id = 'com.xueqiu.android:id/iv_close']"]
        self = args[0]
        try:
            return fun(*args, **kwargs)
        except Exception:
            for element in black_list:
                count = self.finds(MobileBy.XPATH, element)
                if len(count) >= 1:
                    self.find(MobileBy.XPATH, element).click()
                    return fun(*args, **kwargs)

    return run
