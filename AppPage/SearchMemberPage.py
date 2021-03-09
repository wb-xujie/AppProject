# _*_ coding:utf-8 _*_
# author : xiaobai
from appium.webdriver.common.mobileby import MobileBy

from AppPage.InfoPage import InfoPage
from Baseconfig.BaseClass import BaseClass


class SearchMemberPage(BaseClass):

    def Search_goto_InfoPage(self,search):
        self.find(*(MobileBy.XPATH,"//*[@text = '搜索']")).send_keys(search)
        element = self.finds(*(MobileBy.XPATH,"//*[@text = '%s']"%(search)))
        count = len(element)
        print(count)
        if count == 1:
            self.find(*(MobileBy.ID,"com.tencent.wework:id/ebs")).click()
            return InfoPage(self.driver)
        else:
            print("没有找到%s"%(search))


