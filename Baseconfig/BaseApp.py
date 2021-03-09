# _*_ coding:utf-8 _*_
"""
APP初始化
1、启动APP
2、退出APP
3、重启APP

封装方法：
1、滑动查找方法
2、。。。。
"""
from appium import webdriver
from AppPage.MainPage import MainPage
from Baseconfig.BaseClass import BaseClass


class BaseApp(BaseClass):

    # 初始化启动APP
    def NewApp(self):

        if self.driver == None:
            self.desired_caps = {
                    "platformName": "android", #客户端平台
                    "deviceName": "127.0.0.1:7555", #客户端的name
                    "appPackage": "com.tencent.wework",
                    "appActivity": ".launch.WwMainActivity",
                    "dontStopAppOnReset": "True",  #不需要停止APP
                    "noReset": "True",#不重置APP
                    "skipServerInstallation": "true", #跳过设备初始化
                    # "skipDeviceInitialization":"true", #运行前不停止APP
                     }
            # 客户端和appium服务器连接代码
            self.driver = webdriver.Remote("http://localhost:4723/wd/hub", self.desired_caps)
            # self.driver = webdriver.Remote('http://localhost:4723/wd/hub', self.desired_caps)
            self.driver.implicitly_wait(3)
            return self

        else:
            self.driver.launch_app()

    # 初始化一个driver

    # 退出APP
    def StopApp(self):
        self.driver.quit()

    # 重启APP
    def RestartApp(self):
        self.driver.launch_app()

    # 把driver传递给MainPage页
    def goto_MainPage(self):
        return MainPage(self.driver)
