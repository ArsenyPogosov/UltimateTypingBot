import sys
sys.path.append('./src/views/')

from init_bot import dp

import start
import default

from aiogram import types

@dp.message_handler(commands=['start'])
async def start_hook(message: types.Message):
    await start.handler(message)

@dp.message_handler()
async def default_hook(message: types.Message):
    await default.handler(message)


