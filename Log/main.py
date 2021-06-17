from Log import node, Util
import sqlite3 as sq
import time
from enum import Enum, unique
import os
import path
import socket
from inspect import isfunction

# 节点信息模板
nodeInfoTemplate = {
    'nodeId': '节点ID',
    'nodeName': '节点名称',
    'nodeIP': '节点IP',
    'nodePort': '节点端口',
    'mainServerName': '主机名称',
    'mainServerIP': '主机IP',
    'mainServerPort': '主机端口',
    'tick': "访问间隔"
}
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
            nodeMap             : 节点 - 
            logMap              : 日志服务 -
            nodeTemplate        : 节点数据模板
            mainServerName      : 主服务器名
        '''
        self.port = port
        self.storageName = storageName
        self.status = 'init'
        self.tickRange = 24 * 60 * 60
        self.cmdShow = False
        self.nodeMap = {}
        self.logMap = {}
        self.nodeTemplate = nodeInfoTemplate
        self.mainServerName = mainServerName
        self.mainLog = Util(path='test', mainServerName=mainServerName)
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

    # 通过节点ID获取对应节点操作类
    def getLogClassByNodeId(self, nodeId):
        if nodeId in self.logMap:
            return self.logMap[nodeId]
        return self.mainLog

    # 通过节点名称获取对应节点操作类
    def getLogClassByNodeName(self, nodeName):
        if nodeName in self.nodeMap:
            nodeId = self.nodeMap[nodeName]['nodeId']
            return self.getLogClassByNodeId(nodeId)
        else:
            return False

    # 使用节点名称获取节点ID
    def __getNodeIdByName(self, nodeName=''):
        if nodeName != '':
            id = hash(nodeName)
            while True:
                if id in self.logList:
                    id = id + 1
                else:
                    return id

        else:
            return ''

    # 获取traceID
    def getTraceId(self, nodeName=''):
        pass

    # 默认创建/刷新节点列表
    def initModuleList(self):
        pass

    # 添加一个节点
    def addNode(self, nodeInfo):
        nodeId = self.__getNodeIdByName(nodeInfo["nodeId"])
        if nodeId == '':
            return False
        lp = Util(path='test',
                  mainServerName=nodeInfo["mainServerName"],
                  nodeServerName=nodeInfo["nodeName"])
        self.logMap[nodeId] = lp
        node = {
            'nodeId': nodeId,
            'nodeName': nodeInfo["nodeName"],
            'nodeIP': nodeInfo["nodeIP"],
            'nodePort': nodeInfo["nodePort"],
            'mainServerName': nodeInfo["mainServerName"],
            'mainServerIP': nodeInfo["mainServerIP"],
            'mainServerPort': nodeInfo["mainServerPort"],
            'tick': nodeInfo["tick"]
        }
        self.nodeMap[nodeInfo["nodeName"]] = node
        return True

    # 移除一个节点
    def removeNode(self, nodeName, nodeId):
        pass


'''
节点
'''


class LogStorageNode:
    def __init__(self, mainServerName='root', nodeName='node', port='8020'):
        ''' 初始参数
            mainServerName      : 主机名
            nodeName            : 当前节点名称
            port                : 启动端口
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
    ReadyForLink = 0  # 节点上线，等待配置连接中
    Linking = 1  # 链接中
    Missing = 2  # 链接丢失
    ReLink = 3  # 尝试重新链接
    NotFound = 4  # 未找到对应节点or对节点的访问被拒绝
    OnLine = 10  # 节点在线
    OffLine = 20  # 节点离线or已登记的节点日志服务关闭
