# _*_ coding:utf-8 _*_
# author : xiaobai
import logging
import os

from appium.webdriver.common.mobileby import MobileBy
from appium.webdriver.webdriver import WebDriver
import time



class BaseClass:


    # 封装初始化driver
    def __init__(self,driver:WebDriver=None):
        self.driver = driver

    #封装find_element方法
    def find(self, locator, value):
        logging.info("this is test")
        logging.info("find")
        logging.info(locator, value)
        return self.driver.find_element(locator,value)

    def finds(self,locator, value):
        logging.info("this is test")
        logging.info("finds")
        logging.info(locator, value)
        return self.driver.find_elements(locator,value)

    def swipe_Find(self,value,run_time = 5,wait_time = 1000):
        for i in range(run_time):
            if i == 0:
                print(f"滑动{run_time}次未找到")
            try:
                return self.driver.find_element(MobileBy.XPATH,value)
            except:
                win_siez = self.driver.get_window_size()
                width = win_siez['width']
                height = win_siez['height']
                x = int(width / 2)
                y_start = int(height * 3 / 4)
                y_end = int(height / 4)
                self.driver.swipe(x,y_start,x,y_end,wait_time)






