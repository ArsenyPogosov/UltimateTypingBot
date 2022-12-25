import sys
sys.path.append('./src/')

import init_logger
import components.init_postgres
from init_bot import dp
import hooks

from aiogram.utils import executor

def on_shutdown():
    return

if __name__ == '__main__':
    executor.start_polling(dp, on_shutdown=on_shutdown)
