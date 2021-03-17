# _*_ coding:utf-8 _*_
# author: xiaobai

import logging
import time
from logging.handlers import RotatingFileHandler

def LoggerToFile(*args):

    # 创建一个logger
    logger = logging.getLogger('log_to_file')
    # 每次调用log时都清除一下之前的logger，避免打印重复
    logger.handlers.clear()
    # 设置日志的等级
    logger.setLevel(logging.DEBUG)
    # 创建一个hander
    # 设置日志路径+文件名
    filetime = time.strftime("%Y-%m-%d %H-%M-%S")
    log_filename = '../Log/'+ filetime+'.txt'
    handler = logging.handlers.RotatingFileHandler(filename=f'{log_filename}',mode='a',encoding='utf-8')
    # handler = logging.FileHandler(filename=f'{log_filename}',mode='a',encoding='utf-8')
    # 创建日志格式
    formatter = logging.Formatter(fmt="'%(asctime)s' %(filename)s[line:%(lineno)d] %(name)s: %(message)s")
    #将日志格式添加到handler中
    handler.setFormatter(formatter)
    #将handler添加到logger中
    logger.addHandler(handler)
    logger.debug(*args)


def LoggerToConsole(*args):
    logger = logging.getLogger('log_to_console')
    logger.setLevel(logging.DEBUG)
    handler = logging.StreamHandler()
    formatter = logging.Formatter(fmt="'%(asctime)s' %(filename)s[line:%(lineno)d] %(name)s: %(message)s")
    handler.setFormatter(formatter)
    logger.addHandler(handler)
    logger.debug(*args)

def Logger_All(*args):
    # 创建一个logger
    logger = logging.getLogger('log_all')
    # 设置日志的等级
    logger.setLevel(logging.DEBUG)
    # 创建一个hander
    handler_file = logging.FileHandler(filename='xujie.txt', mode='a')
    handler_console = logging.StreamHandler()
    handler_console.setLevel(logging.DEBUG)
    handler_file.setLevel(logging.DEBUG)
    # 创建日志格式
    formatter = logging.Formatter(fmt="'%(asctime)s' %(filename)s[line:%(lineno)d] %(name)s: %(message)s")
    # 将日志格式添加到handler中
    handler_console.setFormatter(formatter)
    handler_file.setFormatter(formatter)
    # 将handler添加到logger中
    logger.addHandler(handler_file)
    logger.addHandler(handler_console)
    logger.debug(*args)