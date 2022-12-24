from components import scores

import logging

async def handler(message):
    username = message.from_user.username
    my_scores = scores.get_user_scores(username)
    my_scores = ['-' if i is None else i for i in my_scores]

    await message.reply(f"Your scores are: {my_scores[0]}, {my_scores[1]}, {my_scores[2]}!")
    logging.info("Send my_scores for "+ message.from_user.username)
