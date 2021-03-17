# _*_ coding:utf-8 _*_
# author : xiaobai
from Baseconfig.BaseClass import BaseClass


class WorkBenchPage(BaseClass):

    # # 接收driver
    # def __init__(self,driver):
    #     self.driver = driver

    # 打卡功能
    def daka(self):
        self.swipe_Find(value="//*[@text = '打卡']").click()