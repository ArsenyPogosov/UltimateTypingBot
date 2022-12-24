import configs

import logging

if configs.LOG_LEVEL == "DEBUG":
    log_level=logging.DEBUG
elif configs.LOG_LEVEL == "INFO":
    log_level=logging.INFO
elif configs.LOG_LEVEL == "WARNING":
    log_level=logging.WARNING
elif configs.LOG_LEVEL == "ERROR":
    log_level=logging.ERROR
elif configs.LOG_LEVEL == "CRITICAL":
    log_level=logging.CRITICAL
logging.basicConfig(level=log_level)
