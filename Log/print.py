import time


class logPrint:
    def __init__(self, mainName="#"):
        self.mainName = mainName + ':'
        pass

    # 普通打印
    def log(self, word):
        print(self.mainName + self.now() + str(word))

    # 获取当前时间
    def now(self):
        return '「' + str(time.time()) + '」'
