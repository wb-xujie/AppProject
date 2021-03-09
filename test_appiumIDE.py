# _*_ coding:utf-8 _*_
from time import sleep
from appium import webdriver
class TestAppiumIDE:

    def setup(self):

        self.desired_caps ={
            "platformName": "Android",
            "platformVersion": "6.0.1",
            "appActivity": ".common.MainActivity",
            "appPackage": "com.xueqiu.android",
            "deviceName": "127.0.0.1:7555",
            "dontStopAppOnReset": "true",
            "noReset": "true",
            "unicodeKeyboard":True,
            "resetKeyboard": True
            }

        self.driver = webdriver.Remote('http://localhost:4723/wd/hub',self.desired_caps)
        self.driver.implicitly_wait(5)

    def teardowm(self):
        self.driver.back()
        self.driver.back()
        self.driver.quit()


    def test_searche(self):

        """
        测试用例描述
        1、打开雪球APP
        2、点击搜索框
        3、在搜索框内输入中文的“阿里巴巴”
        4、在预搜索结果获取“阿里巴巴”，并点击
        5、获取这只香港的阿里巴巴股票价格并断言价格>200
        """
        self.driver.find_element_by_id('com.xueqiu.android:id/tv_search').click()
        sleep(1)
        self.driver.find_element_by_id('com.xueqiu.android:id/search_input_text').send_keys("阿里巴巴")
        sleep(1)
        self.driver.find_element_by_xpath("//*[@resource-id='com.xueqiu.android:id/name' and @text = '阿里巴巴']").click()
        sleep(1)
        price = float(self.driver.find_element_by_id("com.xueqiu.android:id/current_price").text)
        print(price)
        assert price > 200
