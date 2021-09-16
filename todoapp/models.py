from django.db import models
from datetime import datetime,date

# Create your models here.
class Task(models.Model):
    name=models.CharField(max_length=50)
    desc=models.CharField(max_length=100)
    due_date=models.DateField(auto_now_add=False,auto_now=False)
    time = models.TimeField(auto_now_add=False,auto_now=False)


    def __str__(self):
        return self.name
