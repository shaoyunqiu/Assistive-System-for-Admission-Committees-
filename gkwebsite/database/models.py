from __future__ import unicode_literals

from django.db import models
import my_field

# Create your models here.

class Teacher(models.Model):
    account = models.CharField(max_length=50,unique=True)
    password = models.CharField(max_length=50,default="12345678")
    #realName = models.CharField(max_length=20)
    #volunteerList = my_field.ListField(default=[])


