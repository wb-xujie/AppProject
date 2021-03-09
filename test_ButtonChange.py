# _*_ coding:utf-8 _*_

"""
1、打开雪球应用
2、定位首页的搜索框
3、判断搜索框是否可用，并查看搜索框name属性值
4、打印搜索框这个元素的左上角坐标和它的宽高
5、想搜索框输入：alibaba
6、判断【阿里巴巴】是否可见
7、如果可见打印搜索成功并点击，如果不可见，打印搜索失败

"""
from time import sleep

from appium import webdriver


class Testxuqiu:

    def setup(self):
        self.desired_caps = {
            "platformName": "Android",
            "platformVersion": "6.0.1",
            "appActivity": ".common.MainActivity",
            "appPackage": "com.xueqiu.android",
            "deviceName": "127.0.0.1:7555",
            "dontStopAppOnReset": "true",
            "noReset": "true",
            "unicodeKeyboard": True,
            "resetKeyboard": True
        }

        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', self.desired_caps)
        self.driver.implicitly_wait(5)

    def teardowm(self):
        self.driver.back()
        self.driver.back()
        self.driver.quit()

    """
    1、打开雪球应用
    2、定位首页的搜索框
    3、判断搜索框是否可用，并查看搜索框name属性值
    4、打印搜索框这个元素的左上角坐标和它的宽高
    5、想搜索框输入：alibaba
    6、判断【阿里巴巴】是否可见
    7、如果可见打印搜索成功并点击，如果不可见，打印搜索失败

    """
    def test_searchanswer(self):
        element_search = self.driver.find_element_by_id('com.xueqiu.android:id/tv_search')
        # 判断搜索框是否可用
        element_search_enabled = element_search.is_enabled()
        sleep(1)
        print(element_search.text)
        print(element_search.location)
        print(element_search.size)
        if element_search_enabled == True:
            element_search.click()
            sleep(1)
            self.driver.find_element_by_id('com.xueqiu.android:id/search_input_text').send_keys("阿里巴巴")
            sleep(1)
            element_word = self.driver.find_element_by_xpath("//*[@resource-id='com.xueqiu.android:id/name' and @text = '阿里巴巴']")
            element_word_display = element_word.get_attribute("displayed")
            print(element_word_display)
            sleep(1)
            if element_word_display == 'true':
                print("搜索成功")

            else:
                print("搜索失败")

