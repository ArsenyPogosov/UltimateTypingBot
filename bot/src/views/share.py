from components import scores

import logging

async def handler(message):
    id = message.from_user.id
    username = message.from_user.username

    scores.change_user_field(id, 'is_public', "TRUE")

    await message.reply("Твои счета теперь публичны.")
    logging.info("Public scores for " + message.from_user.username)
