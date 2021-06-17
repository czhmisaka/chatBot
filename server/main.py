from fastapi import FastAPI
import sys
import time
from downtool import downtool as down
import os
import uvicorn

from starlette.responses import JSONResponse
sys.path.append("../")
from chatBot import chatBot
# sys.path.append("Log/")
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from Log import *

# uvicorn main:app --reload
app = FastAPI()
bot1 = chatBot({'read_only': False})

# 标准回答
@app.get("/api/bot/{word}")
async def root(word):
    t = time.time()
    text = bot1.getResponse(word).text
    back = JSONResponse(text)
    return back


# 添加下载任务
@app.get("/api/download/{word}")
async def download(word):
    pass



if __name__=='__main__':
    uvicorn.run(app='main:app', host="0.0.0.0",port=8000,reload=True,debug=True)
    bot1.trainerNormal()
