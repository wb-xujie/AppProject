# _*_ coding:utf-8 _*_

from time import sleep
from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction


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

    def test_touchaction(self):
        sleep(1)
        action = TouchAction(self.driver)
        window_size = self.driver.get_window_size()
        print(window_size)
        width = window_size['width']
        height = window_size['height']
        x = int(width/2)
        y_start = int(height * 0.8)
        y_end = int(height * 0.2)

        action.press(x = x , y = y_start).wait(500).move_to(x = x,y = y_end).release().perform()
        sleep(1)

