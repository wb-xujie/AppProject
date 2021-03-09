# _*_ coding:utf-8 _*_
# author : xiaobai
from appium.webdriver.common.mobileby import MobileBy

from Baseconfig.BaseClass import BaseClass


class AddContactPage(BaseClass):
    # # 接收driver
    # def __init__(self,driver:WebDriver):
    #     self.driver = driver

    # 添加成员功能
    def AddContact(self):
        # self.driver.find_element(MobileBy.XPATH,"//*[@text ='手动输入添加']").click()
        # self.driver.find_element(MobileBy.XPATH,"//*[contains(@text ,'姓名')]/..//*[@text = '必填']").send_keys("test3")
        # self.driver.find_element(MobileBy.XPATH,"//*[contains(@text ,'手机')]/..//*[@text = '必填']").send_keys("150234933333")
        # self.driver.find_element(MobileBy.XPATH,"//*[@text = '保存']").click()

        handadd_address = (MobileBy.XPATH, "//*[@text ='手动输入添加']")
        name_address = (MobileBy.XPATH, "//*[contains(@text ,'姓名')]/..//*[@text = '必填']")
        phone_address = (MobileBy.XPATH, "//*[contains(@text ,'手机')]/..//*[@text = '必填']")
        save_address = (MobileBy.XPATH, "//*[@text = '保存']")
        self.find(*handadd_address).click()
        self.find(*name_address).send_keys("test3")
        self.find(*phone_address).send_keys("15023493333")
        self.find(*save_address).click()


    def Check_OK(self):
        # 这种写法比较优秀
        temp = self.find(*(MobileBy.XPATH,"//*[@text = '添加成功']"))
        if temp == 0:
            print("添加失败")
        else:
            print("添加成功")

        self.driver.quit()





