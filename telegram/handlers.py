from aiogram import types
from aiogram.types import Message
from aiogram.dispatcher import Dispatcher
from datetime import datetime
import pytz

# Replace this with your actual timezone
IST = pytz.timezone('Asia/Kolkata')

async def send_signal(message: Message, pair, timeframe, direction, execution_time):
    await message.answer(
        f"✅ SIGNAL\n"
        f"PAIR: {pair}\n"
        f"TIMEFRAME: {timeframe}\n"
        f"DIRECTION: {direction}\n"
        f"EXECUTION: {execution_time}"
    )

def register_handlers(dp: Dispatcher):
    @dp.message_handler(commands=['start'])
    async def handle_start(message: Message):
        await message.answer("👋 Welcome! Please select a currency pair.")

    @dp.message_handler(lambda message: message.text.startswith("PAIR:"))
    async def handle_pair_selection(message: Message):
        await message.answer("⏱ Now select a timeframe (e.g., M1, M5, M15).")

    @dp.message_handler(lambda message: message.text.startswith("TIMEFRAME:"))
    async def handle_timeframe_selection(message: Message):
        now_ist = datetime.now(IST).strftime('%H:%M:%S')
        await send_signal(
            message,
            pair="EUR/USD",
            timeframe="M1",
            direction="BUY",
            execution_time=now_ist
        )
