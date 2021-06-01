# coding=utf-8

import allure


def test_allure():
    print("这是一个测试用例")
    allure.attach.file(r"D:\Programs\AppProject\UI_Framework\Result_screen\2021-04-08-16-44-06.mp44",
                       name="这是一个视频",attachment_type=allure.attachment_type.MP4)