from init_bot import dp

from views import start, task, myscores, default

from aiogram import types

@dp.message_handler(commands=['start'])
async def start_hook(message: types.Message):
    await start.handler(message)

@dp.message_handler(commands=['task'])
async def task_hook(message: types.Message):
    await task.handler(message)

@dp.message_handler(commands=['myscores'])
async def task_myscores(message: types.Message):
    await myscores.handler(message)

@dp.message_handler()
async def default_hook(message: types.Message):
    await default.handler(message)


