from __future__ import unicode_literals

from django.db import models

# Create your models here.


# class RegistrationCode(models.Model):
#     '''
#         registerCode :  Teacher give it to student
#         name : student's name
#         state : registerCode's state
#     '''
#
#     registerCode = models.CharField(max_length=200, primary_key=True)
#     name = models.CharField(max_length=30)
#     state = models.IntegerField()
#
#     NOT_SHARE = 0
#     SHARE_NOT_REGISTER = 1
#     SHARE_REGISTER = 2
#
#     def __unicode__(self):
#         return self.state


class Student(models.Model):
    REGISTER_CODE_UNUSE = 1
    REGISTER_CODE_USED = 2
    REGISTER_CODE_NOT_EXIST = 3

    studentId = models.CharField(max_length=80, primary_key=True)
    realName = models.CharField(max_length=30)
    registerCode = models.CharField(max_length=100, unique=True)
    registerState = models.IntegerField(default=0)