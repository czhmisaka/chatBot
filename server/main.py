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

bot1.trainerByList([
    '你是谁',
    '我是你霸霸！'
])


@app.get("/api/bot/{word}")
async def root(word):
    t = time.time()
    back = JSONResponse(bot1.getResponse(word).text)
    print(time.time()-t)
    return back
