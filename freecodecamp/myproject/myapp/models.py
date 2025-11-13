from enum import UNIQUE

from django.db import models
from django.template.context_processors import request

class Userdata(models.Model):
    Firstname=models.CharField(max_length=15)
    Lastname=models.CharField(max_length=10)
    PhoneNumber=models.IntegerField(unique=True)
    AadharNumber=models.IntegerField(unique=True)
    Age=models.IntegerField()



