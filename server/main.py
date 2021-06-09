from fastapi import FastAPI
import sys

from starlette.responses import JSONResponse
sys.path.append("..")
from chatBot import chatBot

# uvicorn main:app --reload
app = FastAPI()

bot1 = chatBot({'read_only': False})
bot1.trainerNormal()


@app.get("/api/bot/{word}")
async def root(word):
    back = JSONResponse(bot1.getResponse(word).text)
    return back
