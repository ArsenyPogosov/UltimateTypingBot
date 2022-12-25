from components.gen_task import gen_task
from components.task_types import *
from components.task_storage import *

from datetime import datetime
import logging

async def send_task(message, task):
    to_send = " ".join(task)
    to_send = to_send.replace('о', 'o')
    to_send = to_send.replace('с', 'c')
    await message.reply(to_send, protect_content=True)

async def handler(message):
    id = message.from_user.id
    username = message.from_user.username

    if storage.have_task(id):
        await message.reply("У тебя уже есть задача.")
        logging.info(f"User {id} already has a task")
        return

    type = parse(message.get_args())
    task = gen_task(type.value)

    await send_task(message, task)
    storage.give_task(id, TaskData(task, type, datetime.now()))

    logging.info(f"Send {type.name} task to user {id}")
