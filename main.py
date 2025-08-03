from fastapi import FastAPI
from telegram.bot import start_bot

app = FastAPI()

@app.on_event("startup")
async def startup():
    await start_bot()