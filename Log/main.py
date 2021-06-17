from Log import node
import sqlite3 as sq
import time
from enum import Enum, unique
import os
import path
import socket
from inspect import isfunction
'''
czh家庭服务器的日志模块
主机
'''


class LogStorageMain:
    def __init__(self,
                 storageName="LogStorage",
                 mainServerName='root',
                 port='8050'):
        ''' 初始参数
            port                : 默认启动端口
            storageName         : 日志保存地址(搭配Util使用)
            status              : 日志模块服务状态
            tickRange           : txt日志文件分时保存
            cmdShow             : 控制台输出
            nodeList          : 节点列表
        初始参数'''
        self.port = port
        self.storageName = storageName
        self.status = 'init'
        self.tickRange = 10 * 60
        self.cmdShow = False
        self.nodeList = []
        self.mainServerName = mainServerName
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
    def __serverProcess(self):
        pass

    # 启动心跳服务查看节点状态 
    def __beatCheckProcess(self):
        pass

    # 获取traceID
    def getTraceId(self, root='logStorage', module=''):
        pass

    # 默认创建监听列表
    def initModuleList(self):
        pass

    # 添加一个监听节点
    def addNode(self, appList):
        pass

    # 移除一个监听节点
    def removeNode(self, moduleName):
        pass


class LogStorageNode:
    def __init__(self, mainServerName='root', nodeName='node', port='8020'):
        ''' 初始参数
            mainServerName      : 主机名
            nodeName            : 当前节点名称
            port                : 默认启动端口
        初始参数'''
        self.mainServerName = mainServerName
        self.nodeName = nodeName
        self.port = port
        self.IPConfig = self.__getIPConifg()

    # 获取节点配置
    def getConfig(self):
        config = {}
        for x in self:
            if not isfunction(x):
                config[x] = self[x]

    # 获取ip配置
    def __getIPConifg(self):
        IPConfig = {}
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            s.connect(('8.8.8.8', 80))
            IPConfig['ip'] = s.getsockname()[0]
        finally:
            s.close()
        return IPConfig



class NodeStatus(Enum):
    ReadyForLink = 0# 节点上线，等待配置连接中
    Linking = 1     # 链接中
    Missing = 2     # 链接丢失
    ReLink = 3      # 尝试重新链接
    NotFound = 4    # 未找到对应节点or对节点的访问被拒绝
    OnLine = 10     # 节点在线
    OffLine = 20    # 节点离线or已登记的节点日志服务关闭