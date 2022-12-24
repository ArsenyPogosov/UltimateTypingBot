import logging

async def handler(message):
    await message.reply("Hi!")
    logging.info("Hi to "+message.from_user.username)
