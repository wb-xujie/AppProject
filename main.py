# from appium import webdriver
#
# desired_caps = {}
# desired_caps['platformName'] = 'Android'
# desired_caps['platformVersion'] = '6.0.1'
# desired_caps['deviceName'] = '0123456789ABCDEF'
# desired_caps['appPackage'] = 'com.android.settings'
# desired_caps['appActivity'] = 'com.android.settings.Settings'
# driver = webdriver.Remote('http://localhost:4723/wd/hub',desired_caps)
# driver.quit()

import time

print(time.time())
print(time.thread_time())
print(time.localtime())
print(time.asctime())