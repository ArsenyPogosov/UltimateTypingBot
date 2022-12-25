from components.task_types import *

class TaskData:
    def __init__(self, task, task_type, datetime):
        self.task = task
        self.task_type = task_type
        self.datetime = datetime

class TaskStorage:
    def __init__(self):
        self.data = dict()

    def give_task(self, userid, task_data):
        self.data[userid] = task_data
    
    def have_task(self, userid):
        return userid in self.data

    def take_task(self, userid):
        return self.data.pop(userid)

storage = TaskStorage()
