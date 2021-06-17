from fastapi import FastAPI
import sys
import time
from downtool import downtool as down


from starlette.responses import JSONResponse
sys.path.append("..")
from chatBot import chatBot
from Log import LogServerNode,logPrint as lp

# uvicorn main:app --reload
app = FastAPI()

bot1 = chatBot({'read_only': False})
bot1.trainerNormal()

# 标准回答
@app.get("/api/bot/{word}")
async def root(word):
    t = time.time()
    text = bot1.getResponse(word).text
    back = JSONResponse(text)
    print(word,text)
    print(time.time()-t)
    return back

# 添加下载任务
@app.get("/api/download/{word}")
async def download(word):
    pass
