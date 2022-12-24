import sys
sys.path.append('./src/')

import init_logger
from init_bot import dp
import hooks

from aiogram.utils import executor

if __name__ == '__main__':
    executor.start_polling(dp)
