# coding=utf-8
# author=xujie
# datetime = 2021/3/16
import os
import signal
import subprocess
import time
import allure
import pytest



@pytest.fixture()
def record():
    file_time = time.strftime("%Y-%m-%d-%H-%M-%S")
    file_path = "../Result_screen/" + file_time + ".mp4"
    cmd = "scrcpy -r ../Result_screen/" + file_time + ".mp4"
    p = subprocess.Popen(cmd, shell=True)
    yield
    # 执行kill操作
    kill_pid_cmd = "taskkill /IM scrcpy.exe"
    os.system(kill_pid_cmd)
    time.sleep(2)
    allure.attach.file(file_path,name="这是一个视频",attachment_type=allure.attachment_type.MP4)