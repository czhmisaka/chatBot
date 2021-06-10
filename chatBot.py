from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer
from chatterbot.trainers import ListTrainer

class chatBot:
    def __init__(self,config = {}):
        self.bot = ChatBot(
            'Terminal',
            storage_adapter='chatterbot.storage.SQLStorageAdapter',
            logic_adapters=[{
                'import_path': 'chatterbot.logic.BestMatch'#回话逻辑
            }],
            read_only=config['read_only'],
            database_uri='sqlite:///database.db'
        )
        self.trainer = ChatterBotCorpusTrainer(self.bot)
        self.listTrainer = ListTrainer(self.bot)
        pass

        
    def trainerNormal(self):
        self.trainer.train(
            # 'chatterbot.trainers.UbuntuCorpusTrainer',
            "chatterbot.corpus.chinese",
            # "chatterbot.corpus.english"
        )

    def readFile(self):
        pass
    
    def trainerByList(self,arr):
        self.listTrainer.train(arr)

    def learn(self,s):
        self.bot.learn_response(s)

    def getResponse(self,s):
        return self.bot.get_response(s)



# bot1 = chatBot({'read_only':False})
# bot1.trainerNormal()
# a = 'fuck'
# num = 0
# while True:
#     a = bot1.getResponse(a).text
#     num = num + 1
#     print(str(num)+str(' > ')+a)
