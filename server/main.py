from fastapi import FastAPI
import sys
import time

from starlette.responses import JSONResponse
sys.path.append("..")
from chatBot import chatBot

# uvicorn main:app --reload
app = FastAPI()

bot1 = chatBot({'read_only': False})
bot1.trainerNormal()

arr = [[
    '你是谁',
    '我是你霸霸！',
    '你可以叫我TuTu。',
    '我是一个秃头程序员'
]]

arr1 = []
for x in range(1):
    arr1.append('卧槽我听不懂你在说啥！')
    arr1.append('FUUUUUCCCCCCKKKKKKKK!')

bot1.trainerByList(arr1)
for x in arr:
    bot1.trainerByList(x)


@app.get("/api/bot/{word}")
async def root(word):
    t = time.time()
    back = JSONResponse(bot1.getResponse(word).text)
    print(time.time()-t)
    return back
