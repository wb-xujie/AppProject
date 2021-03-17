# _*_ coding:utf-8 _*_
# author:xiaobai
from appium.webdriver.common.mobileby import MobileBy

from UI_Framework.Base.BaseClass import BaseClass
from UI_Framework.Page.MarketPage import MarketPage


class MainPage(BaseClass):
    # 进入行情页面
    def goto_market(self):
        # 截图确认main界面
        self.screenshot()
        # self.find_click(MobileBy.XPATH,"//*[@resource-id = 'com.xueqiu.android:id/post_status']")
        # self.find_click(MobileBy.XPATH,"//*[@resource-id ='android:id/tabs']/.//*[contains(@text ,'行情')]")
        self.ReadFile('../Data/MainPage.yaml','goto_market')
        return MarketPage(self.driver)

