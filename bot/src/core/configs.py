import os
from dotenv import load_dotenv

directory='configs'
for config in os.listdir(directory):
    file = os.path.join(directory, config)
    if os.path.isfile(file):
        load_dotenv(file, encoding='utf8')

BOT_TOKEN = os.getenv('BOT_TOKEN')

LOG_LEVEL = os.getenv('LOG_LEVEL')

DB_USER = os.getenv('DB_USER')
DB_PASS = os.getenv('DB_PASS')
DB_HOST = os.getenv('DB_HOST')
DB_PORT = os.getenv('DB_PORT')
DB_NAME = os.getenv('DB_NAME')
