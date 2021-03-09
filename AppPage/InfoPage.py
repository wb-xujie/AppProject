# _*_ coding:utf-8 _*_
# author : xiaobai
from appium.webdriver.common.mobileby import MobileBy

from Baseconfig.BaseClass import BaseClass


class InfoPage(BaseClass):

    def DeletMember(self):
        # 点击更多
        self.find(*(MobileBy.ID,"com.tencent.wework:id/iga")).click()
        # 点击编辑
        self.find(*(MobileBy.XPATH,"//*[@text = '编辑成员']")).click()
        self.search = self.find(*(MobileBy.XPATH,"//*[contains(@text, '姓名')]/../*[@index = '2']")).text
        self.find(*(MobileBy.XPATH,"//*[@text = '删除成员']")).click()
        # 点击确认
        self.find(*(MobileBy.ID,"com.tencent.wework:id/bpc")).click()

    def Check_OK(self):
        count = len(self.finds(*(MobileBy.XPATH,"//*[@text = '无搜索结果']")))
        if count ==1:
            print("删除成功")

        else:
            print("删除失败")

