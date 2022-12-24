from init_bot import dp

from views import start, help, task, myscores, top, share, noshare, default

from aiogram import types

@dp.message_handler(commands=['start'])
async def start_hook(message: types.Message):
    await start.handler(message)

@dp.message_handler(commands=['help'])
async def help_hook(message: types.Message):
    await help.handler(message)

@dp.message_handler(commands=['task'])
async def task_hook(message: types.Message):
    await task.handler(message)

@dp.message_handler(commands=['myscores'])
async def myscores_hook(message: types.Message):
    await myscores.handler(message)

@dp.message_handler(commands=['top'])
async def top_hook(message: types.Message):
    await top.handler(message)

@dp.message_handler(commands=['share'])
async def share_hook(message: types.Message):
    await share.handler(message)

@dp.message_handler(commands=['noshare'])
async def noshare_hook(message: types.Message):
    await noshare.handler(message)

@dp.message_handler()
async def default_hook(message: types.Message):
    await default.handler(message)


