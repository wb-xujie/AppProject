# _*_ coding:utf-8 _*_
# author : xiaobai
from appium.webdriver.common.mobileby import MobileBy

from AppPage.AddContactPage import AddContactPage
from AppPage.SearchMemberPage import SearchMemberPage
from Baseconfig.BaseClass import BaseClass


class AddressListPage(BaseClass):

    # # 接收driver
    # def __init__(self,driver:WebDriver):
    #     self.driver = driver

    # 添加成员
    def goto_AddContactPage(self):
        # self.driver.find_element(MobileBy.XPATH,"//*[@text ='添加成员']").click()
        addcontact_address = (MobileBy.XPATH, "//*[@text ='添加成员']")
        self.find(*addcontact_address).click()
        return AddContactPage(self.driver)


    def goto_SearchMemberPage(self):
        self.find(*(MobileBy.ID,"com.tencent.wework:id/igk")).click()
        return SearchMemberPage(self.driver)
