import sqlite3 as sql
import os
from .print import logPrint as lp
import logging

# 注册一个终端打印的类
ulp = lp(mainName='Util module')
'''
日志服务 基础操作工具
1. 同步写入txt+sql
2. 分类提示
3. 提供错误枚举类型
4. 默认带入traceId，提供当前使用者标记
'''


class Util():
    def __init__(self, storageName, path=''):
        '''初始参数
        sqlStorageName      : 数据库保存名称 
        txtStorageName      : txt格式日志保存标识名
        txtPath             : txt格式日志保存路径
        初始参数'''
        self.sqlLogStorage = storageName
        self.txtLogStorage = storageName
        self.txtPath = path + '/Log/' + str(storageName)
        __checkFile(self.txtPath)
        logging.basicConfig(level=logging.DEBUG,filename=self.txtLogStorage,filemode='w',format='%(name)s[%(levelname)s]:%(message)s')
        pass
    # 添加一条新的记录
    def addNewRecord(self,data):
        logging.info(data)
        return True

    # 通过traceID搜索 该模块下的记录
    def searchByTraceId(self,traceId = ''):
        pass


# 判断文件是否存在，不存在则创建，可创建文件夹
def __checkFile(path):
    try:
        if os.path.exists(path):
            return True
        else:
            f = open(path, 'w')
            f.close()
            return True
    except IOError:
        ulp.log('IOError in __checkFile[' + str(path) + ']')


# 写入文档数据
def __writeTxt(path, data):
    try:
        with open(path, 'w') as f:
            f.writelines(str(data) + '\n')
    except IOError:
        ulp.log('IOError in __writeTxt[' + str(path) + ',' + str(data) + ']')
        return False
    except:
        ulp.log('OtherError in __writeTxt[' + str(path) + ',' + str(data) +
                ']')
        return False
    else:
        return True
