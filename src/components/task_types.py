import enum
import logging

class TaskType(enum.IntEnum):
    SMALL=100
    MEDIUM=250
    LARGE=500

def parse(type):
    type = type.upper()
    try:
        return TaskType[type]
    except:
        logging.warning(type + " is not a task type, I am using small.")
        return TaskType['SMALL']
