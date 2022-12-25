from components import scores

import logging

async def handler(message):
    id = message.from_user.id
    username = message.from_user.username
    scores.init_user(id, username)

    await message.reply("Привет! Я @UltimateTypingBot! Набери /help для помощи.")
    logging.info(f"Hi to user {id}")
