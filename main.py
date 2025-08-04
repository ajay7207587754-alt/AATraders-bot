from fastapi import FastAPI
from telegram.bot import start_bot

app = FastAPI()

@app.on_event("startup")
async def startup():
    await start_bot()
import os

bot_token = os.getenv("8389318322:AAFBjVX1GLkww28iUUQqY8K58aIonmC4EJ4")
if not bot_token:
    raise Exception("Telegram bot token not found in environment variables")

# Example: initializing your bot
from telegram import Bot
bot = Bot(token=bot_token)

# Or if using python-telegram-bot library, something like:
# updater = Updater(token=bot_token)
