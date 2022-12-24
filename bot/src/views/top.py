from components.task_types import*
from components import scores

from tabulate import tabulate
import logging

def make_table(table):
    return tabulate(table, headers=["user", "small", "medium", "large"], tablefmt="fancy_grid")

async def handler(message):
    top = scores.get_best('score_' + parse(message.get_args()).name.lower(), 10)

    await message.reply("\nCurrent top: \n```\n" + make_table(top) + "\n```", parse_mode="Markdown")
    logging.info("Send top to " + message.from_user.username)
