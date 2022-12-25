from components import scores

import logging

async def handler(message):
    id = message.from_user.id
    username = message.from_user.username

    scores.change_user_field(id, 'is_public', "FALSE")

    await message.reply("Твои счета теперь приватны.")
    logging.info(f"Public scores for user {id}")
