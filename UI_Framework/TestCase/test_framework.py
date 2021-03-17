# _*_ coding:utf-8 _*_
"""
"""
from UI_Framework.Base.BaseApp import BaseApp


class Testxueqiu:

    def setup(self):
        self.app = BaseApp()
        self.main = self.app.NewApp().goto_MainPage()

    def teardown(self):
        pass

    def test_market(self,record):
        self.main.goto_market().goto_search().Serch()