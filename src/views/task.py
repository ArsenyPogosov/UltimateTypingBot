from components.gen_task import gen_task
from components.task_types import *
from components.task_storage import *

from datetime import datetime
import logging

async def send_task(message, task):
    await message.reply(" ".join(task))

async def handler(message):
    username = message.from_user.username
    if storage.have_task(username):
        await message.reply("You already have a task.")
        logging.info("User " + username + " already has a task")
        return

    type = parse(message.get_args())
    task = gen_task(type.value)

    await send_task(message, task)
    storage.give_task(username, TaskData(task, type, datetime.now()))

    logging.info("Send " + type.name + " task to " + message.from_user.username)
