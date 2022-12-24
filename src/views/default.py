import logging

async def handler(message):
    await message.reply("I agree")
    logging.info("Agreed with " + message.from_user.username)
