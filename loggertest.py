# #  _*_ coding:utf-8 _*_
# import logging  # 引入logging模块
# # 将信息打印到控制台上
# logging.basicConfig(level=logging.DEBUG)
# logging.debug(u"苍井空")
# logging.info(u"麻生希")
# logging.warning(u"小泽玛利亚")
# logging.error(u"桃谷绘里香")
# logging.critical(u"泷泽萝拉")
#
# import logging  # 引入logging模块
# logging.basicConfig(level=logging.DEBUG,
#                     format='%(asctime)s - %(filename)s[line:%(lineno)d] - %(levelname)s: %(message)s')  # logging.basicConfig函数对日志的输出格式及方式做相关配置
# # 由于日志基本配置中级别设置为DEBUG，所以一下打印信息将会全部显示在控制台上
# logging.info('this is a loggging info message')
# logging.debug('this is a loggging debug message')
# logging.warning('this is loggging a warning message')
# logging.error('this is an loggging error message')
# logging.critical('this is a loggging critical message')

# import logging  # 引入logging模块
# import os.path
# import time
# # 第一步，创建一个logger
# logger = logging.getLogger()
# logger.setLevel(logging.DEBUG)  # Log等级总开关
# # 第二步，创建一个handler，用于写入日志文件
# rq = time.strftime('%Y%m%d%H%M', time.localtime(time.time()))
# print(os.getcwd())
# log_path = os.path.dirname(os.getcwd()) + '/Logs/'
# log_name = log_path + rq + '.log'
# logfile = log_name
# fh = logging.FileHandler(logfile, mode='w')
# fh.setLevel(logging.DEBUG)  # 输出到file的log等级的开关
#
# ch = logging.StreamHandler()
# ch.setLevel(logging.DEBUG)
# # 第三步，定义handler的输出格式
# formatter = logging.Formatter("%(asctime)s - %(filename)s[line:%(lineno)d] - %(levelname)s: %(message)s")
# fh.setFormatter(formatter)
# ch.setFormatter(formatter)
# # 第四步，将logger添加到handler里面
# logger.addHandler(fh)
# logger.addHandler(ch)
# # 日志
#
# a = 1+2
# logger.debug(f"a = 1+2 ret:a = {a}")
# logger.info('this is a logger info message')
# logger.warning('this is a logger warning message')
# logger.error('this is a logger error message')
# logger.critical('this is a logger critical message')

"""
日志处理流程
1、创建一个logger
2、设置logger的等级
3、创建一个合适的Handler
4、设置每个Handler的日志等级
5、设置日志格式formatter
6、向handler中添加5中的格式
7、将handler添加到logger中
8、打印输出

"""

# import logging
#
# # 创建一个logger
# logger = logging.getLogger('xujie')
# # 设置logger的日志等级
# logger.setLevel(logging.DEBUG)
#
# # 创建一个Handler
# handler = logging.StreamHandler()
# # 设置handler的日志等级
# handler.setLevel(logging.DEBUG)
# # 创建日志输出格式
# formatter = logging.Formatter(fmt="%(asctime)s - %(filename)s[%(lineno)d]-%(name)s: %(message)s",datefmt="%Y-%m-%d %X")
# # 将格式添加到handler
# handler.setFormatter(formatter)
# # 将handler添加到logger中
# logger.addHandler(handler)
#
# logger.debug("xujie")
# logger.info("test")
# logger.error("error")


# import logging
# # 创建logger，如果参数为空则返回root logger
# logger = logging.getLogger("nick")
# logger.setLevel(logging.DEBUG)  # 设置logger日志等级
# # 创建handler
# fh = logging.FileHandler("test.log", encoding="utf-8")
# ch = logging.StreamHandler()
# # 设置输出日志格式
# formatter = logging.Formatter(
#     fmt="%(asctime)s %(name)s %(filename)s %(message)s",
#     datefmt="%Y/%m/%d %X"
# )
# # 注意 logging.Formatter的大小写
#
# # 为handler指定输出格式，注意大小写
# fh.setFormatter(formatter)
# ch.setFormatter(formatter)
# # 为logger添加的日志处理器
# logger.addHandler(fh)
# logger.addHandler(ch)
# # 输出不同级别的log
# logger.warning("泰拳警告")
# logger.info("提示")
# logger.error("错误")

import logging
# # 创建一个logger
# logger = logging.getLogger('xujie')
# # 设置日志的等级
# logger.setLevel(logging.DEBUG)
# # 创建一个hander
# handler = logging.FileHandler(filename='xujie.txt', mode='a')
# # 创建日志格式
# formatter = logging.Formatter(fmt="'%(asctime)s' %(filename)s[%(lineno)d] %(name)s: %(message)s")
# # 将日志格式添加到handler中
# handler.setFormatter(formatter)
# # 将handler添加到logger中
# logger.addHandler(handler)
logger = logging.getLogger('xujie')
logger.setLevel(logging.DEBUG)
handler = logging.StreamHandler()
formatter = logging.Formatter(fmt="'%(asctime)s' %(filename)s[%(lineno)d] %(name)s: %(message)s")
handler.setFormatter(formatter)
logger.addHandler(handler)

logger.warning("泰拳警告")
logger.info("提示")
logger.error("错误")