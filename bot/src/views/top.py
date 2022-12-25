from components.task_types import*
from components import scores

from tabulate import tabulate
import logging

def make_table(table):
    return tabulate(table, headers=["user", "small", "medium", "large"], tablefmt="simple")

async def handler(message):
    id = message.from_user.id
    top = scores.get_best('score_' + parse(message.get_args()).name.lower(), 10)

    await message.reply("\nТекущий топ: \n```\n" + make_table(top) + "\n```", parse_mode="Markdown")
    logging.info(f"Send top to user {id}")
