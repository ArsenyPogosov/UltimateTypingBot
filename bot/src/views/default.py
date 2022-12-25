from components.task_storage import storage
from components.give_score import give_score
from components.update_score import update_score

from datetime import datetime
import logging

async def handler(message):
    id = message.from_user.id
    username = message.from_user.username

    if not storage.have_task(id):
        logging.info("User " + username + " send unwanted message.")
        return

    task_data = storage.take_task(id)
    score, why = give_score(task_data.task, message.text, datetime.now().timestamp() - task_data.datetime.timestamp())
    
    await message.reply(f"Твой счет равен {why}{score}!")
    logging.info(f"User {id} get score {score}.")
    
    if update_score(id, task_data.task_type, score):
        await message.reply("Новый рекорд!")
        logging.info(f"User {id} got new record.")
