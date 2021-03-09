# _*_ coding:utf-8 _*_
# author : xiaobai
from appium.webdriver.common.mobileby import MobileBy
from appium.webdriver.webdriver import WebDriver



class BaseClass:

    # 封装初始化driver
    def __init__(self,driver:WebDriver=None):
        self.driver = driver

    #封装find_element方法
    def find(self, locator,value):
        return self.driver.find_element(locator,value)

    def finds(self,locator,value):
        return self.driver.find_elements(locator,value)