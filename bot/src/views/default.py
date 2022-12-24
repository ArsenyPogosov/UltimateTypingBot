from components.task_storage import storage
from components.give_score import give_score

from datetime import datetime
import logging

async def handler(message):
    username = message.from_user.username
    if not storage.have_task(username):
        logging.info("User " + username + " send unwanted message.")
        return

    task_data = storage.take_task(username)
    score, why = give_score(task_data.task, message.text, datetime.now().timestamp() - task_data.datetime.timestamp())
    
    await message.reply(f"Your score is {why}{score}!")
    logging.info(f"{username} get score {score}.")
