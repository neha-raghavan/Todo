from django.db import models
from datetime import datetime,date
from django.contrib.auth.models import User,AbstractBaseUser, UserManager


# Create your models here.
class Task(models.Model):
    name=models.CharField(max_length=50)
    desc=models.CharField(max_length=100)
    due_date=models.DateField(auto_now_add=False,auto_now=False)
    time = models.TimeField(auto_now_add=False,auto_now=False)


    def __str__(self):
        return self.name


class Users(models.Model):
    name=models.CharField(max_length=200,null=True)
    phone=models.CharField(max_length=200,null=True)
    email=models.CharField(max_length=200,null=True)
    password = models.CharField(max_length=50)
    profile_pic=models.ImageField(default="profile_pic.png",null=True,blank=True)



    def __str__(self):
        return self.name
