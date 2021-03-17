import time
from time import sleep

import allure
import yaml
from appium.webdriver.common.mobileby import MobileBy
from appium.webdriver.webdriver import WebDriver

from UI_Framework.Base import logger
from UI_Framework.Base.Blacklist import Black_list


class BaseClass:


    # 封装初始化driver
    def __init__(self,driver:WebDriver=None):
        self.driver = driver

    #封装find_element方法
    @Black_list
    def find(self, locator, value):
        logger.LoggerToFile("find:"+ "locator:"+locator + "  value:"+value)
        return self.driver.find_element(locator,value)


    def finds(self,locator, value):
        logger.LoggerToFile("finds:" + "locator:"+locator + "  value:"+value)
        return self.driver.find_elements(locator,value)

    def find_click(self,locator,value):
        return self.find(locator,value).click()

    def find_and_send(self,locator,value,text):
        return  self.find(locator,value).send_keys(text)

    def swipe_find(self,value,run_time = 5,wait_time = 1000):
        for i in range(run_time):
            if i == 0:
                print(f"滑动{run_time}次未找到")
            try:
                return self.find(MobileBy.XPATH,value)
            except:
                win_siez = self.driver.get_window_size()
                width = win_siez['width']
                height = win_siez['height']
                x = int(width / 2)
                y_start = int(height * 3 / 4)
                y_end = int(height / 4)
                self.driver.swipe(x,y_start,x,y_end,wait_time)

    def ReadFile(self,path,function):
        with open(f'{path}','r',encoding='utf-8') as f:
            function_data = yaml.load(f)
        # steps = function_data[f'{function}']
        steps = function_data.get(f'{function}')
        for step in steps:
            if step['action']=='find_click':
                self.find_click(step.get('locator'),step.get('value'))

            elif step['action']=='find':
                self.find(step['locator'],step['value'])

            elif step['action']=='finds':
                self.finds(step['locator'],step['value'])

            elif step['action']=='find_and_send':
                self.find_and_send(step['locator'],step['value'],step['text'])

            elif step['action']=='swipe_find':
                self.swipe_find(step['value'])

            else:
                print("命令无法识别")

    def screenshot(self):
        sleep(1)
        f_time = time.strftime("%Y-%m-%d-%H-%M-%S")
        file_name = f_time+".png"
        file_path = f'../Result_screen/{f_time}.png'

        self.driver.get_screenshot_as_file(file_path)
        allure.attach.file(file_path,name=file_name,attachment_type=allure.attachment_type.PNG)

