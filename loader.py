import logging
import os
from aiogram import Bot, Dispatcher
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from handlers import router
from middlewares.register_check import RegisterCheck

BOT_TOKEN = os.environ.get('BOT_TOKEN')

logging.basicConfig(level=logging.INFO)
bot = Bot(token=BOT_TOKEN)
scheduler = AsyncIOScheduler()
dp = Dispatcher(sheduler=scheduler)
dp.include_router(router)

# dp.message.middleware(RegisterCheck())
# dp.callback_query.middleware(RegisterCheck())