# _*_ coding:utf-8 _*_
from appium.webdriver.common.mobileby import MobileBy

from UI_Framework.Base.BaseClass import BaseClass
from UI_Framework.Page.SearchPage import SearchPage


class MarketPage(BaseClass):

    def goto_search(self):
        # 截图确认Market界面
        self.screenshot()
        # self.find_click(MobileBy.XPATH,"//*[@resource-id = 'com.xueqiu.android:id/action_search']")
        self.ReadFile('../Data/MarketPage.yaml',"goto_search")
        return SearchPage(self.driver)


