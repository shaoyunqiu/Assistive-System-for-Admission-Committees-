# coding=utf-8

from models import *
from database import models
from django.db import IntegrityError

# Student
STUDENT_ATTR_LIST = ['realName']

def addRegisterCodeInStudent(regis_code, dic):
    try:
        student = Student.objects.create(registerCode=regis_code)
    except:
        return False
    for attr in STUDENT_ATTR_LIST:
        setattr(student, attr, dic.get(attr))
    student.full_clean()
    student.save()
    return True

def getRegisterCodeStateInStudent(regis_code):
    try:
        student = Student.objects.get(registerCode=regis_code)
        return student.registerState
    except:
        return Student.REGISTER_CODE_NOT_EXIST


def setAttrInStudent(student_id, dic):
    try:
        student = Student.objects.create(studentId=student_id)
    except IntegrityError:
        student = Student.objects.get(pk=student_id)
    for attr in STUDENT_ATTR_LIST:
        setattr(student, attr, dic.get(attr))
    student.full_clean()
    student.save()








