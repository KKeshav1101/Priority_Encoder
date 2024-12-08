from django.db import models
import datetime as dt


# Create your models here.
class Task(models.Model):
    task_desc=models.CharField(max_length=100)
    task_type=models.CharField(max_length=50)
    task_date=models.DateField()
    task_due=models.DateField()
    task_weight=models.FloatField()
    accname = models.CharField(max_length=50)
    completed=models.BooleanField(default=False)

    def show(self):
        return f'''
        Task Description: {self.task_desc}
        Task Type: {self.task_type}
        Task Date: {self.task_date}
        Task Due Date: {self.task_due}
        Task Weight: {self.task_weight}'''

class Account(models.Model):
    username=models.CharField(max_length=25)
    tasklist=models.CharField(max_length=255)

