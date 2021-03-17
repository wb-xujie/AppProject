# coding=utf-8
# author=xujie
# datetime = 2021/3/16
import json
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
    # p = os.popen(cmd)
    yield
    os.kill(p.pid, signal.CTRL_C_EVENT)
    allure.attach.file(file_path, name=file_time, attachment_type=allure.attachment_type.MP4)
