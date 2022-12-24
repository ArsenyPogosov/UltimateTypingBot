from core import configs

from sqlalchemy import create_engine
import logging

db_string = 'postgresql://{}:{}@{}:{}/{}'.format(configs.DB_USER, configs.DB_PASS, configs.DB_HOST, configs.DB_PORT, configs.DB_NAME)
db = create_engine(db_string)
logging.info('Connected to postgres.')
