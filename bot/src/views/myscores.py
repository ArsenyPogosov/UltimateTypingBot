from components import scores

from tabulate import tabulate
import logging

def make_table(table):
    return tabulate([table], headers=["small", "medium", "large"], tablefmt="simple")

async def handler(message):
    id = message.from_user.id
    username = message.from_user.username

    my_scores = scores.get_user_scores(id)

    await message.reply(f"Твои счета:\n```\n" + make_table(my_scores) + "\n```", parse_mode="Markdown")
    logging.info(f"Send my_scores for user {id}")
