# _*_ coding:utf-8 _*_
# author : xiaobai
from appium.webdriver.common.mobileby import MobileBy

from AppPage.AddressListPage import AddressListPage
from AppPage.WorkBenchPage import WorkBenchPage
from Baseconfig.BaseClass import BaseClass


class MainPage(BaseClass):

    # # 接收driver
    # def __init__(self,driver:WebDriver):
    #     self.driver = driver
    # 消息页面
    # 预留
    def goto_NewsPage(self):
        # self.driver.find_element(MobileBy.XPATH,"//*[@class = 'android.view.ViewGroup']//*[@text = '消息']").click()
        news_address= (MobileBy.XPATH, "//*[@class = 'android.view.ViewGroup']//*[@text = '消息']")
        self.find(*news_address)
    # 通讯录页面
    def goto_AddressListPage(self):
        # self.driver.find_element(MobileBy.XPATH,"//*[@text = '通讯录']").click()
        element_address = (MobileBy.XPATH, "//*[@text = '通讯录']")
        self.find(*element_address).click()
        return AddressListPage(self.driver)
    # 工作台页面
    def goto_WorkBenchPage(self):
        # self.driver.find_element(MobileBy.XPATH,"//*[@text = '工作台']").click()
        workbench_address = (MobileBy.XPATH, "//*[@text = '工作台']")
        self.find(*workbench_address).click()
        return WorkBenchPage(self.driver)


    # 我的页面
    # 预留
    def goto_MinePage(self):
        # self.driver.find_element(MobileBy.XPATH,"//*[@class = 'android.view.ViewGroup']//*[@text = '我']").click()
        mine_address = (MobileBy.XPATH, "//*[@class = 'android.view.ViewGroup']//*[@text = '我']")
        self.find(*mine_address).click()

