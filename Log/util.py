import sqlite3 as sql




'''
日志文件同步操作工具
'''
class Util():
    def __init__(self,storageName):
        '''初始参数
        sqlStorageName      : 数据库保存名称 
        txtStorageName      : txt格式日志保存文件路径
        初始参数'''
        self.sqlLogStorage = storageName
        self.txtLogStorage = storageName
        pass
    
    def addNewRecord(self):
        pass

# 判断文件夹是否存在，不存在则创建
def mkdirFolder(path):
    pass

# 判断文件是否存在，不存在则创建
def mkdirFile(path):
    pass

# 写入文档数据
def __writeTxt(path,data):
    pass
