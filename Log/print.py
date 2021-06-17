import logging
import time
from uvicorn.main import main
import os

class logPrint:
    def __init__(self,logPath="", mainName="", nodeName=""):
        if mainName == "":
            return False
        self.mainName = mainName
        self.nodeName = nodeName
        self.logPath = logPath
        self.logClass = mainName + '.' + nodeName
        self.logObj = logging
        self.logFormat = self.logObj.Formatter(fmt='%(levelname)s-%(name)s【%(asctime)s】:%(message)s', datefmt='%Y-%m-%d %H:%M:%S')
        self.logObj.basicConfig(level=self.logObj.INFO)
        self.log = self.logObj.getLogger(self.logClass)
        self.handler = self.logObj.FileHandler(logPath+'/index.log')
        self.handler.setFormatter(self.logFormat)
        self.log.addHandler(self.handler)

    # 配置文件地址
    def baseConfig(self,logPath=""):
        self.logObj.basicConfig(filemode='a', filename=logPath+'/index.log',level=self.logObj.INFO)

    # 各种打印
    def info(self, word):
        self.log.info(self.mainName + word)

    def err(self, word):
        self.log.error(self.mainName + word)

    def warn(self, word):
        self.log.warn(self.mainName + word)

    # 获取当前时间
    def now(self):
        return str(time.time())

    # 检查文件夹
    def __checkFile(self,path):
        try:
            if os.path.exists(path):
                return True
            else:
                f = open(path, 'w')
                f.close()
                return True
        except IOError:
            self.log.info('IOError in __checkFile[' + str(path) + ']')


