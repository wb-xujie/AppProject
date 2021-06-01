# _*_ coding:utf-8 _*_
"""
"""
import allure

from UI_Framework.Base.BaseApp import BaseApp

@allure.feature("雪球")
class Testxueqiu:

    def setup(self):
        self.app = BaseApp()
        self.main = self.app.NewApp().goto_MainPage()

    def teardown(self):
        # self.app.StopApp()
        pass
    @allure.story("搜索")
    def test_Serch(self, record):
        with allure.step("步骤1"):
            self.main.goto_market().goto_search().Serch()

    def test_market(self,record):
        self.main.goto_market()