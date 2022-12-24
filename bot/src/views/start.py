from components import scores

import logging

async def handler(message):
    username = message.from_user.username
    scores.init_user(username)

    await message.reply("Hi! I am UltimateTypingBot! Type /help for help.")
    logging.info("Hi to "+message.from_user.username)
