from appium.webdriver.common.mobileby import MobileBy

from UI_Framework.Base.BaseClass import BaseClass


class SearchPage(BaseClass):

    def Serch(self):
        # 截图确认search界面
        self.screenshot()
        # self.find_and_send(MobileBy.XPATH,"//*[@resource-id = 'com.xueqiu.android:id/search_input_text']",'alibaba')
        self.ReadFile('../Data/SearchPage.yaml',"Search")
        # 截图最终确认用例执行结果
        self.screenshot()

