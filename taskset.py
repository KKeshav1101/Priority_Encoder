import datetime as dt
class Task:
    def __init__(self, desc, type, due, wt,tstitle):
        self.task_desc = desc
        self.task_type = type
        self.task_date = dt.datetime.now()
        self.task_due = due
        self.task_weight = wt
        self.task_set = tstitle
        # self.isDone = False

    def show(self):
        return f'''
        Task Description: {self.task_desc}
        Task Type: {self.task_type}
        Task Date: {self.task_date}
        Task Due Date: {self.task_due}
        Task Weight: {self.task_weight}
        Task Completed: {self.isDone}'''


class TaskSet:
    def __init__(self, title, accname):
        self.title = title
        self.tasklist = []
        self.date = dt.datetime.now()
        self.accname = accname

    def show(self):
        print(self.title)
        for task in self.tasklist:
            print(task)

    def add_task(self, task):
        self.tasklist.append(task)

    def remove_task(self, task):
        self.tasklist.remove(task)
