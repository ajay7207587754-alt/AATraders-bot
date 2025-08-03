from aiogram import Bot, Dispatcher
from telegram.handlers import register_handlers

TOKEN = "8458886661:AAH-V-2umARUVLo2_ayWqPtHKNLhvNhbMyQ"
bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

async def start_bot():
    register_handlers(dp)
    await dp.start_polling()