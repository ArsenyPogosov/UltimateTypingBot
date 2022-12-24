from components import scores

import logging

async def handler(message):
    username = message.from_user.username
    scores.change_user_field(username, 'is_public', "TRUE")

    await message.reply("Your scores are public now.")
    logging.info("Public scores for " + message.from_user.username)
