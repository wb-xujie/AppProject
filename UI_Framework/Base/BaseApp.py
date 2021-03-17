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
import yaml
from appium import webdriver

from UI_Framework.Base.BaseClass import BaseClass
from UI_Framework.Page.MainPage import MainPage


class BaseApp(BaseClass):

    # 初始化启动APP
    def NewApp(self):

        if self.driver == None:
            with open("../Data/Data.yml", 'r', encoding="utf-8") as file:
                data = yaml.safe_load(file)
                self.desired_caps = data["desired_caps"]
                self.host = data["localhost"]["host"]
            # # 客户端和appium服务器连接代码
            self.driver = webdriver.Remote(f"{self.host}", self.desired_caps)
            self.driver.implicitly_wait(5)
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
