import logging as log
import sqlite3 as sq
import time
from enum import Enum, unique
import os
import path
'''
czh家庭服务器的日志模块
主机
'''


class LogStorage:
    def __init__(self, storageName="LogStorage"):
        ''' 初始参数
            port                : 默认启动端口
            storageName         : 日志保存地址(搭配Util使用)
            status              : 日志模块服务状态
            tickRange           : txt日志文件分时保存
            cmdShow             : 控制台输出
        初始参数'''
        self.port = '8050'
        self.storageName = storageName
        self.status = 'init'
        self.tickRange = 10 * 60
        self.cmdShow = False
        pass

    # 正常日志
    def log(self):
        pass

    # 错误日志
    def err(self):
        pass

    # 警告日志
    def warn(self):
        pass

    # 启动日志模块守护线程
    def __helpProcess(self):
        pass

    # 启动日志查看服务器
    def __serverProcess():
        pass