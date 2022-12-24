import configs

from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher

bot = Bot(token=configs.BOT_TOKEN)
dp = Dispatcher(bot)

