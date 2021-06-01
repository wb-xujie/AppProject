# from time import sleep
#
# from appium import webdriver
# from appium.webdriver.extensions.android.gsm import GsmCallActions
#
# desired_caps = {}
# desired_caps['platformName'] = 'Android'
# desired_caps['platformVersion'] = '9.0'
# desired_caps['deviceName'] = 'CKNA432248HDA0047'
# desired_caps['appPackage'] = 'com.autonavi.amapauto'
# desired_caps['appActivity'] = '.MainMapActivity'
# driver = webdriver.Remote('http://localhost:4723/wd/hub',desired_caps)


def demo(fun):
    def run(*args,**kwargs):
        print('这是一个装饰器')
        fun(*args,**kwargs)
        print("结束了")
    return run





@demo
def a(a):
    print(f'我是{a}')

def test():
    a('张三')