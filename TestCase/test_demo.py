# _*_ coding:utf-8 _*_
"""
"""
from Baseconfig.BaseApp import BaseApp


class TestWeiXin():

    # 添加成员测试用例
    def test_AddMember(self):
        self.app = BaseApp()
        self.main = self.app.NewApp().goto_MainPage()
        self.Contact = self.main.goto_AddressListPage().goto_AddContactPage()
        self.Contact.AddContact()
        self.Contact.Check_OK()

    #删除成员测试用例
    def test_deletMember(self):
        self.app = BaseApp()
        self.main = self.app.NewApp().goto_MainPage()
        self.Delet = self.main.goto_AddressListPage().goto_SearchMemberPage().Search_goto_InfoPage(search="test3")
        self.Delet.DeletMember()
        self.Delet.Check_OK()
